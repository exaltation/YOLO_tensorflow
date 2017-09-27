import sys
import YOLO_tiny_tf

yolo = YOLO_tiny_tf.YOLO_TF()

yolo.disp_console = True
yolo.imshow = True

if len(sys.argv) > 1:
    yolo.tofile_img = sys.argv[1] + '.processed.jpg'
    yolo.filewrite_img = True
    yolo.detect_from_file(sys.argv[1])
