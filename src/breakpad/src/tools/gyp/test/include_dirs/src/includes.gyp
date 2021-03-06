# Copyright (c) 2009 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'includes',
      'type': 'executable',
      'dependencies': [
        'subdir/subdir_includes.gyp:subdir_includes',
      ],
      'include_dirs': [
        '.',
        'inc1',
        'subdir/inc2',
      ],
      'sources': [
        'includes.c',
      ],
    },
  ],
}
