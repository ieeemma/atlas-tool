import struct
import json
import sys

READER_BLOCK = [0x03, 0x74, 0x54, 0x65, 0x78, 0x74, 0x75, 0x72, 0x65, 0x41, 0x74, 0x6C, 0x61, 0x73, 0x43, 0x6F,
                0x6E, 0x74, 0x65, 0x6E, 0x74, 0x2E, 0x54, 0x65, 0x78, 0x74, 0x75, 0x72, 0x65, 0x41, 0x74, 0x6C,
                0x61, 0x73, 0x52, 0x65, 0x61, 0x64, 0x65, 0x72, 0x2C, 0x20, 0x54, 0x65, 0x78, 0x74, 0x75, 0x72,
                0x65, 0x41, 0x74, 0x6C, 0x61, 0x73, 0x43, 0x6F, 0x6E, 0x74, 0x65, 0x6E, 0x74, 0x50, 0x43, 0x2C,
                0x20, 0x56, 0x65, 0x72, 0x73, 0x69, 0x6F, 0x6E, 0x3D, 0x31, 0x2E, 0x30, 0x2E, 0x30, 0x2E, 0x30,
                0x2C, 0x20, 0x43, 0x75, 0x6C, 0x74, 0x75, 0x72, 0x65, 0x3D, 0x6E, 0x65, 0x75, 0x74, 0x72, 0x61,
                0x6C, 0x2C, 0x20, 0x50, 0x75, 0x62, 0x6C, 0x69, 0x63, 0x4B, 0x65, 0x79, 0x54, 0x6F, 0x6B, 0x65,
                0x6E, 0x3D, 0x6E, 0x75, 0x6C, 0x6C, 0x00, 0x00, 0x00, 0x00, 0x75, 0x54, 0x65, 0x78, 0x74, 0x75,
                0x72, 0x65, 0x41, 0x74, 0x6C, 0x61, 0x73, 0x43, 0x6F, 0x6E, 0x74, 0x65, 0x6E, 0x74, 0x2E, 0x54,
                0x65, 0x78, 0x74, 0x75, 0x72, 0x65, 0x52, 0x65, 0x67, 0x69, 0x6F, 0x6E, 0x52, 0x65, 0x61, 0x64,
                0x65, 0x72, 0x2C, 0x20, 0x54, 0x65, 0x78, 0x74, 0x75, 0x72, 0x65, 0x41, 0x74, 0x6C, 0x61, 0x73,
                0x43, 0x6F, 0x6E, 0x74, 0x65, 0x6E, 0x74, 0x50, 0x43, 0x2C, 0x20, 0x56, 0x65, 0x72, 0x73, 0x69,
                0x6F, 0x6E, 0x3D, 0x31, 0x2E, 0x30, 0x2E, 0x30, 0x2E, 0x30, 0x2C, 0x20, 0x43, 0x75, 0x6C, 0x74,
                0x75, 0x72, 0x65, 0x3D, 0x6E, 0x65, 0x75, 0x74, 0x72, 0x61, 0x6C, 0x2C, 0x20, 0x50, 0x75, 0x62,
                0x6C, 0x69, 0x63, 0x4B, 0x65, 0x79, 0x54, 0x6F, 0x6B, 0x65, 0x6E, 0x3D, 0x6E, 0x75, 0x6C, 0x6C,
                0x00, 0x00, 0x00, 0x00, 0x2F, 0x4D, 0x69, 0x63, 0x72, 0x6F, 0x73, 0x6F, 0x66, 0x74, 0x2E, 0x58,
                0x6E, 0x61, 0x2E, 0x46, 0x72, 0x61, 0x6D, 0x65, 0x77, 0x6F, 0x72, 0x6B, 0x2E, 0x43, 0x6F, 0x6E,
                0x74, 0x65, 0x6E, 0x74, 0x2E, 0x52, 0x65, 0x63, 0x74, 0x61, 0x6E, 0x67, 0x6C, 0x65, 0x52, 0x65,
                0x61, 0x64, 0x65, 0x72, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01]


class AtlasDataItem:
    def __init__(self):
        self.reader_type_1 = 0
        self.name_size = 0
        self.name = "" * self.name_size
        
        self.reader_type_2 = 0
        self.bounds_x = 0
        self.bounds_y = 0
        self.bounds_w = 0
        self.bounds_h = 0

        self.origin_x = 0
        self.origin_y = 0

        self.origin_size_x = 0
        self.origin_size_y = 0
        

class AtlasFile:
    
    def __init__(self):
        pass

    def write(self, file_path):

        def write_char(value):
            return struct.pack("c", value.encode("utf-8"))

        def write_int(value):
            return struct.pack("B", value)

        def write_uint32(value):
            return struct.pack("I", value)

        def write_float(value):
            return struct.pack("f", value)

        def write_7bit(value):
            result = []
            if value == 0:
                result.append(0)
            else:
                while value != 0:
                    temp = value & 0b01111111
                    value >>= 7
                    if value != 0:
                        temp |= 0b10000000
                    result.append(temp)
            return result

    
        # XNB header
        header = b""
        
        header += write_char(self.format_identifier[0])
        header += write_char(self.format_identifier[1])
        header += write_char(self.format_identifier[2])
        header += write_char(self.platform)
        header += write_int(self.xnb_version)
        header += write_int(self.flag)

        # XNB type readers
        type_reader = b""
        type_reader += bytes(READER_BLOCK)
            
        # XNB data
        data = b""
        
        data += write_uint32(len(self.atlas_data_items))
        
        for adi in self.atlas_data_items:
            data += write_int(adi.reader_type_1)
            data += write_int(adi.name_size)
            for char in adi.name:
                data += write_char(char)
            
            data += write_int(adi.reader_type_2)
            data += write_uint32(adi.sprite_x)
            data += write_uint32(adi.sprite_y)
            data += write_uint32(adi.sprite_h)
            data += write_uint32(adi.sprite_w)

            data += write_float(adi.bounding_box_x)
            data += write_float(adi.bounding_box_y)
            data += write_float(adi.bounding_box_w)
            data += write_float(adi.bounding_box_h)

        data += write_uint32(self.max_width)
        data += write_uint32(self.max_height)

        header += write_uint32(len(data) + len(type_reader) + 10) # not sure where im missing 10 bytes? its a constant offset though, so its fine

        with open(file_path, 'wb') as f:
            f.write(header)
            f.write(type_reader)
            f.write(data)
    
    def read(self, file_path):
        with open(file_path, 'rb') as f:

            def read_char():
                return struct.unpack("c", f.read(1))[0].decode("utf-8")

            def read_int():
                return struct.unpack("B", f.read(1))[0]

            def read_uint32():
                return struct.unpack("I", f.read(4))[0]

            def read_float():
                return struct.unpack("f", f.read(4))[0]

            def read_7bit():
                output = 0
                while True:
                        byte = int.from_bytes(f.read(1), "little")
                        output = output << 7
                        output |= byte & 0x7f
                        if byte & 0x80 == 0:
                                break
                return output

            # XNB header
            self.format_identifier = read_char()
            self.format_identifier += read_char()
            self.format_identifier += read_char()
            self.platform = read_char()
            self.xnb_version = read_int()
            self.flag = read_int()
            self.file_size = read_uint32()

            # XNB type readers
            self.type_readers = []
            type_reader_count = read_7bit()
            
            for i in range(len(READER_BLOCK)-1):
                read_char()
            
            # XNB data
            self.atlas_data_items = []
            atlas_frame_count = read_uint32()
            
            for _ in range(atlas_frame_count):
                adi = AtlasDataItem()
                adi.reader_type_1 = read_int()
                adi.name_size = read_int()
                adi.name = ""
                for _ in range(adi.name_size):
                    adi.name += read_char()
                
                adi.reader_type_2 = read_int()
                adi.sprite_x = read_uint32()
                adi.sprite_y = read_uint32()
                adi.sprite_h = read_uint32()
                adi.sprite_w = read_uint32()

                adi.bounding_box_x = read_float()
                adi.bounding_box_y = read_float()
                adi.bounding_box_w = read_float()
                adi.bounding_box_h = read_float()

                self.atlas_data_items.append(adi)

            self.max_width = read_uint32()
            self.max_height = read_uint32()

    def write_json(self, file_path):
        atlas_json = {}
        atlas_json["base_w"] = self.max_width
        atlas_json["base_h"] = self.max_height
        
        atlas_json["frames"] = {}
        for atlas in self.atlas_data_items:
            atlas_json["frames"][atlas.name] = {

                "sprite_x": atlas.sprite_x,
                "sprite_y": atlas.sprite_y,
                "sprite_w": atlas.sprite_w,
                "sprite_h": atlas.sprite_h,

                "bounding_box_x": atlas.bounding_box_x,
                "bounding_box_y": atlas.bounding_box_y,
                "bounding_box_w": atlas.bounding_box_w,
                "bounding_box_h": atlas.bounding_box_h,

            }
            
        with open(file_path, 'w') as file:
            json.dump(atlas_json, file, indent=8)

    def read_json(self, file_path):

        self.format_identifier = "XNB"
        self.platform = "w"
        self.xnb_version = 5
        self.flag = 0

        with open(file_path, 'r') as file:
            atlas_json = json.load(file)

        self.max_width = atlas_json["base_w"]
        self.max_height = atlas_json["base_h"]

        self.atlas_data_items = []

        for frame_name in atlas_json["frames"]:
            adi = AtlasDataItem()
            
            adi.reader_type_1 = 2
            adi.name_size = len(frame_name)
            adi.name = frame_name
            
            adi.reader_type_2 = 3
            adi.sprite_x = atlas_json["frames"][frame_name]["sprite_x"]
            adi.sprite_y = atlas_json["frames"][frame_name]["sprite_y"]
            adi.sprite_h = atlas_json["frames"][frame_name]["sprite_h"]
            adi.sprite_w = atlas_json["frames"][frame_name]["sprite_w"]

            adi.bounding_box_x = atlas_json["frames"][frame_name]["bounding_box_x"]
            adi.bounding_box_y = atlas_json["frames"][frame_name]["bounding_box_y"]
            adi.bounding_box_w = atlas_json["frames"][frame_name]["bounding_box_w"]
            adi.bounding_box_h = atlas_json["frames"][frame_name]["bounding_box_h"]

            self.atlas_data_items.append(adi)




if len(sys.argv) == 1:
    print("Usage: \n\tatlas.exe filename.xnb\n\tatlas.exe filename.json")
    raise SystemExit
else:
    file_path = sys.argv[1]

atlas = AtlasFile()
if file_path.endswith(".xnb"):
    atlas.read(file_path)
    atlas.write_json(file_path[:-4]+".json")
        
elif file_path.endswith(".json"):
    atlas.read_json(file_path)
    atlas.write(file_path[:-5]+".xnb")
else:
    print("Usage: \n\tatlas.exe filename.xnb\n\tatlas.exe filename.json")
    raise SystemExit
