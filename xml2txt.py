#!cai dat pylabel
#!pip install pylabel

from pylabel import importer
'''
dataset = importer.ImportVOC('/home/dungdinh/yolo_v5/datasets/box/labels')
dataset.export.ExportToYoloV5()
'''


def xml2txt(folder_xml):
    dataset = importer.ImportVOC(folder_xml)
    dataset.export.ExportToYoloV5()
    #dataset.export.ExportToVoc()


if __name__ == "__main__":
    xml2txt('/home/dungdinh/Documents/prj_tach_chu_cccd/model_cccd/datasets/data/xml')

