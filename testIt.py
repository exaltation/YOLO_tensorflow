import sys
import YOLO_small_tf

yolo = YOLO_small_tf.YOLO_TF()

yolo.disp_console = True

if len(sys.argv) > 2:
    yolo.tofile_img = sys.argv[1] + '.processed.jpg'
    yolo.filewrite_img = True

    yolo.filewrite_txt = True
    yolo.tofile_txt = sys.argv[1] + '.processed.txt'

    yolo.detect_from_file(sys.argv[1])

    yolo.tofile_img = sys.argv[2] + '.processed.jpg'
    yolo.tofile_txt = sys.argv[2] + '.processed.txt'

    yolo.detect_from_file(sys.argv[2])
