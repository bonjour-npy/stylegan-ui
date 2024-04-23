imagenet_templates = [
    'a bad photo of a {}.',
    'a sculpture of a {}.',
    'a photo of the hard to see {}.',
    'a low resolution photo of the {}.',
    'a rendering of a {}.',
    'graffiti of a {}.',
    'a bad photo of the {}.',
    'a cropped photo of the {}.',
    'a tattoo of a {}.',
    'the embroidered {}.',
    'a photo of a hard to see {}.',
    'a bright photo of a {}.',
    'a photo of a clean {}.',
    'a photo of a dirty {}.',
    'a dark photo of the {}.',
    'a drawing of a {}.',
    'a photo of my {}.',
    'the plastic {}.',
    'a photo of the cool {}.',
    'a close-up photo of a {}.',
    'a black and white photo of the {}.',
    'a painting of the {}.',
    'a painting of a {}.',
    'a pixelated photo of the {}.',
    'a sculpture of the {}.',
    'a bright photo of the {}.',
    'a cropped photo of a {}.',
    'a plastic {}.',
    'a photo of the dirty {}.',
    'a jpeg corrupted photo of a {}.',
    'a blurry photo of the {}.',
    'a photo of the {}.',
    'a good photo of the {}.',
    'a rendering of the {}.',
    'a {} in a video game.',
    'a photo of one {}.',
    'a doodle of a {}.',
    'a close-up photo of the {}.',
    'a photo of a {}.',
    'the origami {}.',
    'the {} in a video game.',
    'a sketch of a {}.',
    'a doodle of the {}.',
    'a origami {}.',
    'a low resolution photo of a {}.',
    'the toy {}.',
    'a rendition of the {}.',
    'a photo of the clean {}.',
    'a photo of a large {}.',
    'a rendition of a {}.',
    'a photo of a nice {}.',
    'a photo of a weird {}.',
    'a blurry photo of a {}.',
    'a cartoon {}.',
    'art of a {}.',
    'a sketch of the {}.',
    'a embroidered {}.',
    'a pixelated photo of a {}.',
    'itap of the {}.',
    'a jpeg corrupted photo of the {}.',
    'a good photo of a {}.',
    'a plushie {}.',
    'a photo of the nice {}.',
    'a photo of the small {}.',
    'a photo of the weird {}.',
    'the cartoon {}.',
    'art of the {}.',
    'a drawing of the {}.',
    'a photo of the large {}.',
    'a black and white photo of a {}.',
    'the plushie {}.',
    'a dark photo of a {}.',
    'itap of a {}.',
    'graffiti of the {}.',
    'a toy {}.',
    'itap of my {}.',
    'a photo of a cool {}.',
    'a photo of a small {}.',
    'a tattoo of the {}.',
]

part_templates = [
    'the paw of a {}.',
    'the nose of a {}.',
    'the eye of the {}.',
    'the ears of a {}.',
    'an eye of a {}.',
    'the tongue of a {}.',
    'the fur of the {}.',
    'colorful {} fur.',
    'a snout of a {}.',
    'the teeth of the {}.',
    'the {}s fangs.',
    'a claw of the {}.',
    'the face of the {}',
    'a neck of a {}',
    'the head of the {}',
]

imagenet_templates_small = [
    'a photo of a {}.',
    'a rendering of a {}.',
    'a cropped photo of the {}.',
    'the photo of a {}.',
    'a photo of a clean {}.',
    'a photo of a dirty {}.',
    'a dark photo of the {}.',
    'a photo of my {}.',
    'a photo of the cool {}.',
    'a close-up photo of a {}.',
    'a bright photo of the {}.',
    'a cropped photo of a {}.',
    'a photo of the {}.',
    'a good photo of the {}.',
    'a photo of one {}.',
    'a close-up photo of the {}.',
    'a rendition of the {}.',
    'a photo of the clean {}.',
    'a rendition of a {}.',
    'a photo of a nice {}.',
    'a good photo of a {}.',
    'a photo of the nice {}.',
    'a photo of the small {}.',
    'a photo of the weird {}.',
    'a photo of the large {}.',
    'a photo of a cool {}.',
    'a photo of a small {}.',
]

##################################################
# 加入带有域特征的自定义的prompts模板供Mapper学习时使用 #
##################################################
ffhq_disney_templates = [
    "a cartoon photo of a disney character",
    "disney character face with smooth curves",
    "dreamlike style disney character photo",
    "cute disney character face",
    "disney face with few wrinkles",
    "disney face with thin lips",
    "close up of disney character face with big eyes",
    "disney character portrait in vibrant colors",
    "disney character face in soft lighting",
    "innocent and cute disney character face",
    "exaggerated proportions close up of disney character features",
    "dreamlike disney style character portrait",
    "close up of disney character face with big round eyes",
    "flawless smooth disney character face",
    "perfectly smooth disney character face",
    "playful close up of disney character features",
    "exaggerated proportions disney character face",
    "disney style character portrait in soft lighting",
    "simplified disney character face lacking details",
    "close up of full red disney character lips",
    "disney style smooth curves forming character face",
    "vibrant colors close up of disney character features",
    "dreamlike disney style character half body",
    "simplified cartoon disney character face",
    "soft lighting shaping disney character face",
    "exaggerated big eyes close up of disney character face",
    "wrinkle-free smooth disney character face",
    "innocent cute disney style character portrait",
    "full red cartoon disney character lips",
    "simplified disney style close up of character features",
    "dreamlike soft lighting disney character portrait",
    "exaggerated proportions close up of disney character features",
    "simplified lacking details disney character face",
    "playful disney style character features",
    "vibrant colors shaping disney character facial features",
    "innocent cute disney style character half body",
    "smooth curves forming perfect disney character face",
    "big round eyes close up of disney character face",
    "dreamlike disney style character full body",
    "flawlessly smooth shaping of disney character face",
    "playful close up of disney style big eyes",
    "soft lighting on disney character body parts",
    "simplified lacking details disney character features",
    "exaggerated proportions close up of disney character body parts",
    "vibrant colors shaping disney character body parts",
    "close up of red full disney style lips",
    "smooth curves forming disney character body parts",
    "dreamlike disney style close up of character hands",
    "flawlessly smooth shaping of disney character body parts",
    "playful close up of disney style character hands",
    "soft lighting on disney character feet close up",
    "simplified lacking details disney character hands",
    "exaggerated proportions close up of disney character feet",
    "vibrant colors shaping disney character feet",
    "dreamlike disney style close up of character hair",
    "smooth curves forming disney character hair",
    "flawlessly smooth shaping of disney character hair",
    "playful close up of disney style character hair",
    "soft lighting on texture of disney character hair",
    "simplified lacking details disney character hair",
    "a cute disney character photo without eye-bags",
    "a cute disney character photo without eyelashes",
    "a cute disney character photo without eye-bags",
    "a cute disney character photo without eyelashes",
]