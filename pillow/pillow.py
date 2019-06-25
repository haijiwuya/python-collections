from PIL import Image
def fill_images(image):
    """填充正方形白色背景图片"""
    width, height = image.size  # 获取图片的宽高
    side = max(width, height)   # 对比宽和高哪个大

    # 新生成的图片是正方形的，边长取大的，背景设置白色
    new_image = Image.new(image.mode, (side, side), color='white')

    # 根据尺寸不同，将原图片仿佛新建的空白图片中部
    if width > height:
        new_image.paste(image, (0, int((side - height) / 2)))
    else:
        new_image.paste(image, (int((side-width) / 2), 0))
    return new_image

def cut_images(image):
    """切割大正方形图"""
    width, height = image.size
    one_thid_width = int(width / 3)     # 三分之一正方形像素

    # 保存每一个小切图的区域
    box_list = []

    """
    切图区域是矩形，位置由对角线的两个点(左上，右下)确定，
    而crop()实际要传入四个参数(left,upper,right,lower)
    """
    for x in range(3):
        for y in range(3):
            left = x * one_thid_width   # 左像素
            upper = y * one_thid_width  # 上像素
            right = (x + 1) * one_thid_width    # 右像素
            lower = (y + 1) * one_thid_width    # 下像素
            box = (left, upper, right, lower)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list