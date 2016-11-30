import os

REMAP_FONTS = [
    ('overpass-mono-bold.ttf', 'OverpassMono-Bold.ttf'),
    ('overpass-mono-light.ttf', 'OverpassMono-Light.ttf'),
    ('overpass-mono-regular.ttf', 'OverpassMono-Regular.ttf'),
    ('overpass-mono-semibold.ttf', 'OverpassMono-SemiBold.ttf'),
    ('overpass-bold-italic.ttf', 'Overpass-BoldItalic.ttf'),
    ('overpass-bold.ttf', 'Overpass-Bold.ttf'),
    ('overpass-extrabold-italic.ttf', 'Overpass-ExtraBoldItalic.ttf'),
    ('overpass-extrabold.ttf', 'Overpass-ExtraBold.ttf'),
    ('overpass-extralight-italic.ttf', 'Overpass-ExtraLightItalic.ttf'),
    ('overpass-extralight.ttf', 'Overpass-ExtraLight.ttf'),
    ('overpass-heavy-italic.ttf', 'Overpass-BlackItalic.ttf'),
    ('overpass-heavy.ttf', 'Overpass-Black.ttf'),
    ('overpass-italic.ttf', 'Overpass-Italic.ttf'),
    ('overpass-light-italic.ttf', 'Overpass-LightItalic.ttf'),
    ('overpass-light.ttf', 'Overpass-Light.ttf'),
    ('overpass-regular.ttf', 'Overpass-Regular.ttf'),
    ('overpass-semibold-italic.ttf', 'Overpass-SemiBoldItalic.ttf'),
    ('overpass-semibold.ttf', 'Overpass-SemiBold.ttf'),
    ('overpass-thin-italic.ttf', 'Overpass-ThinItalic.ttf'),
    ('overpass-thin.ttf', 'Overpass-Thin.ttf'),
]

for old_name, new_name in REMAP_FONTS:
    if old_name in os.listdir('.'):
        os.rename(os.path.join('.', old_name), os.path.join('.', new_name))
        print 'renamed %s to %s' % (old_name, new_name)
print 'Done renaming'
