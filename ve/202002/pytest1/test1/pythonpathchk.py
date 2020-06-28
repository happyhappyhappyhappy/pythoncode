import os
import sys
print('Now Using {} '.format(sys.path))
# print('OS Path Now Dir {}'.format(os.path.dirname(__file__)))
# print(os.path.join(os.path.dirname(__file__), '..'))
print('abspath {}'.format(os.path.abspath(__file__)))
print('dirname+abspath {}'.format(os.path.dirname(os.path.abspath(__file__))))
