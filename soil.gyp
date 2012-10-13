#
# soil.gyp
#
{
  'targets': [
    {
      'target_name': 'soil_lib',
      'product_name': 'soil',
      'type': 'static_library',
      'conditions': [
        ['OS=="win"', {
          'defines': [
            'WIN32',
          ],
        }], # OS=="win"
      ],
      'sources': [
        'src/src/image_DXT.c',
        'src/src/image_DXT.h',
        'src/src/image_helper.c',
        'src/src/image_helper.h',
        'src/src/SOIL.c',
        'src/src/SOIL.h',
        'src/src/stb_image_aug.c',
        'src/src/stb_image_aug.h',
        'src/src/stbi_DDS_aug.h',
        'src/src/stbi_DDS_aug_c.h',
        #'src/src/test_SOIL.cpp',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'src/src/',
        ],
      },
    },
  ],
}
# vim:sts=2:sw=2:norl
