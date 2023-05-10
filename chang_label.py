import xml.etree.ElementTree as ET
import glob

def change_label(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    root[6][0].text = 'tl'
    root[7][0].text = 'tr'
    root[8][0].text = 'br'
    root[9][0].text = 'bl'
    tree.write(xml_path)

def process(folder_path):
    for file in glob.glob(folder_path + '/*.xml'):
        print(file)
        change_label(file)

if __name__ == "__main__":
    process('/home/dungdinh/Documents/prj_tach_chu_cccd/model_detect_corner/box_goc_split')


