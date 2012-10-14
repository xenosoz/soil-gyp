#
# soil.gyp
#
{
  'targets': [
    {
      'target_name': 'soil_static',
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
        'soil-20080707/src/image_DXT.c',
        'soil-20080707/src/image_DXT.h',
        'soil-20080707/src/image_helper.c',
        'soil-20080707/src/image_helper.h',
        'soil-20080707/src/SOIL.c',
        'soil-20080707/src/SOIL.h',
        'soil-20080707/src/stb_image_aug.c',
        'soil-20080707/src/stb_image_aug.h',
        'soil-20080707/src/stbi_DDS_aug.h',
        'soil-20080707/src/stbi_DDS_aug_c.h',
        #'soil-20080707/src/test_SOIL.cpp',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'soil-20080707/src/',
        ],
      },
    },
  ],
}
# vim:sts=2:sw=2:norl
