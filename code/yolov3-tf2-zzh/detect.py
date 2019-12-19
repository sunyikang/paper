import time
from absl import app, flags, logging
from absl.flags import FLAGS
import cv2
import numpy as np
import tensorflow as tf
from yolov3_tf2.models import (
    YoloV3, YoloV3Tiny
)
from yolov3_tf2.dataset import transform_images
from yolov3_tf2.utils import draw_outputs
import platformer

flags.DEFINE_string('classes', './data/coco.names', 'path to classes file')
flags.DEFINE_string('weights', './checkpoints/yolov3.tf',
                    'path to weights file')
flags.DEFINE_boolean('tiny', False, 'yolov3 or yolov3-tiny')
flags.DEFINE_integer('size', 416, 'resize images to')
flags.DEFINE_string('image', './data/street.jpg', 'path to input image')
flags.DEFINE_string('output', './output.jpg', 'path to output image')
flags.DEFINE_integer('num_classes', 80, 'number of classes in the model')


def _shrink_dimension(boxes, scores, classes, nums):
    len0 = nums[0]
    classes = classes[0][0:len0]
    logging.info(classes)

    mask1 = classes.numpy() == 0
    logging.info(mask1)

    classes = classes[0:len0]
    classes = tf.boolean_mask(classes, mask1)
    logging.info(classes)

    scores = scores[0][0:len0]
    scores = tf.boolean_mask(scores, mask1)
    logging.info(scores)

    boxes = boxes[0][0:len0]
    boxes = tf.boolean_mask(boxes, mask1)
    logging.info(boxes)

    return boxes, scores, classes

def _print_person_score_boxes(boxes, scores):
    for i in range(len(scores)):
        logging.info(' [{}]: {}, {}'.format(i, scores[i], np.array(boxes[i])))

def _draw_output_image(boxes, scores, classes, class_names):
    img = cv2.imread(FLAGS.image)
    img = draw_outputs(img, (boxes, scores, classes), class_names)
    cv2.imwrite(FLAGS.output, img)
    logging.info('output saved to: {}'.format(FLAGS.output))

def main(_argv):
    if platformer.get_platform() != 'OS X':
        physical_devices = tf.config.experimental.list_physical_devices('GPU')
        if len(physical_devices) > 0:
            tf.config.experimental.set_memory_growth(physical_devices[0], True)

    logging.info(FLAGS.num_classes)
    
    if FLAGS.tiny:
        yolo = YoloV3Tiny(classes=FLAGS.num_classes)
    else:
        yolo = YoloV3(classes=FLAGS.num_classes)

    yolo.load_weights(FLAGS.weights)
    logging.info('weights loaded')

    class_names = [c.strip() for c in open(FLAGS.classes).readlines()]
    logging.info('classes loaded')

    img = tf.image.decode_image(open(FLAGS.image, 'rb').read(), channels=3)
    img = tf.expand_dims(img, 0)
    img = transform_images(img, FLAGS.size)

    t1 = time.time()
    boxes, scores, classes, nums = yolo(img)
    t2 = time.time()
    logging.info('time: {}'.format(t2 - t1))
    
    boxes, scores, classes = _shrink_dimension(boxes, scores, classes, nums)
    
    _print_person_score_boxes(boxes, scores)
    
    _draw_output_image(boxes, scores, classes, class_names)


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
