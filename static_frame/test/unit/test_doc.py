import doctest
import os
import typing as tp

api_example_str = '''


#-------------------------------------------------------------------------------
# import and setup

>>> import static_frame as sf
>>> _display_config_active = sf.DisplayActive.get()
>>> sf.DisplayActive.set(sf.DisplayConfig(type_color=False))
>>> import numpy as np
>>> import static_frame as sf

#-------------------------------------------------------------------------------
# documentation introduction

#start_immutability

>>> import static_frame as sf
>>> import numpy as np

>>> s = sf.Series((67, 62, 27, 14), index=('Jupiter', 'Saturn', 'Uranus', 'Neptune'), dtype=np.int64)
>>> s #doctest: +NORMALIZE_WHITESPACE
<Series>
<Index>
Jupiter  67
Saturn   62
Uranus   27
Neptune  14
<<U7>    <int64>
>>> s['Jupiter'] = 68
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Series' object does not support item assignment
>>> s.iloc[0] = 68
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'InterfaceGetItem' object does not support item assignment
>>> s.values[0] = 68
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: assignment destination is read-only

#end_immutability

#start_assign
>>> s.assign['Jupiter'](69) #doctest: +NORMALIZE_WHITESPACE
<Series>
<Index>
Jupiter  69
Saturn   62
Uranus   27
Neptune  14
<<U7>    <int64>
>>> s.assign['Uranus':](s['Uranus':] - 2) #doctest: +NORMALIZE_WHITESPACE
<Series>
<Index>
Jupiter  67
Saturn   62
Uranus   25
Neptune  12
<<U7>   <int64>
>>> s.assign.iloc[[0, 3]]((68, 11)) #doctest: +NORMALIZE_WHITESPACE
<Series>
<Index>
Jupiter  68
Saturn   62
Uranus   27
Neptune  11
<<U7>    <int64>

#end_assign


#-------------------------------------------------------------------------------
# series

#start_Series-via_str.capitalize()
>>> s = sf.Series(('lepton', 'lepton', 'quark'), index=('muon', 'tau', 'strange'))
>>> s.via_str.capitalize()
<Series>
<Index>
muon     Lepton
tau      Lepton
strange  Quark
<<U7>    <<U6>

#end_Series-via_str.capitalize()


#start_Series-via_str.center()
>>> s = sf.Series(('lepton', 'lepton', 'quark'), index=('muon', 'tau', 'strange'))
>>> s.via_str.center(20, '-')
<Series>
<Index>
muon     -------lepton-------
tau      -------lepton-------
strange  -------quark--------
<<U7>    <<U20>

#end_Series-via_str.center()


#start_Series-via_str.endswith()
>>> s = sf.Series(('lepton', 'lepton', 'quark'), index=('muon', 'tau', 'strange'))
>>> s.via_str.endswith('ton')
<Series>
<Index>
muon     True
tau      True
strange  False
<<U7>    <bool>

#end_Series-via_str.endswith()


#start_Series-via_str.isdigit()
>>> s = sf.Series(('lepton', 'lepton', 'quark'), index=('muon', 'tau', 'strange'))
>>> s.via_str.isdigit()
<Series>
<Index>
muon     False
tau      False
strange  False
<<U7>    <bool>

#end_Series-via_str.isdigit()


#start_Series-via_str.ljust()
>>> s = sf.Series(('lepton', 'lepton', 'quark'), index=('muon', 'tau', 'strange'))
>>> s.via_str.ljust(10, '-')
<Series>
<Index>
muon     lepton----
tau      lepton----
strange  quark-----
<<U7>    <<U10>

#end_Series-via_str.ljust()


#start_Series-via_str.rjust()
>>> s = sf.Series(('lepton', 'lepton', 'quark'), index=('muon', 'tau', 'strange'))
>>> s.via_str.rjust(10, '-')
<Series>
<Index>
muon     ----lepton
tau      ----lepton
strange  -----quark
<<U7>    <<U10>

#end_Series-via_str.rjust()


#start_Series-via_str.startswith()
>>> s = sf.Series(('lepton', 'lepton', 'quark'), index=('muon', 'tau', 'strange'))
>>> s.via_str.startswith('lep')
<Series>
<Index>
muon     True
tau      True
strange  False
<<U7>    <bool>

#end_Series-via_str.startswith()


#start_Series-via_str.title()
>>> s.via_str.title()
<Series>
<Index>
muon     Lepton
tau      Lepton
strange  Quark
<<U7>    <<U6>

#end_Series-via_str.title()



#start_Series-via_str.upper()
>>> s = sf.Series(('lepton', 'lepton', 'quark'), index=('muon', 'tau', 'strange'))
>>> s.via_str.upper()
<Series>
<Index>
muon     LEPTON
tau      LEPTON
strange  QUARK
<<U7>    <<U6>

#end_Series-via_str.upper()




#start_Series-from_dict()
>>> sf.Series.from_dict(dict(Mercury=167, Neptune=-200), dtype=np.int64)
<Series>
<Index>
Mercury  167
Neptune  -200
<<U7>    <int64>

#end_Series-from_dict()


#start_Series-__init__()
>>> sf.Series((167, -200), index=('Mercury', 'Neptune'), dtype=np.int64)
<Series>
<Index>
Mercury  167
Neptune  -200
<<U7>    <int64>

#end_Series-__init__()


#start_Series-from_items()
>>> sf.Series.from_items(zip(('Mercury', 'Jupiter'), (4879, 12756)), dtype=np.int64)
<Series>
<Index>
Mercury  4879
Jupiter  12756
<<U7>    <int64>

#end_Series-from_items()


#start_Series-from_element()
>>> sf.Series.from_element('lepton', index=('electron', 'muon', 'tau'))
<Series>
<Index>
electron lepton
muon     lepton
tau      lepton
<<U8>    <<U6>

#end_Series-from_element()



#start_Series-items()
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'), dtype=np.int64)
>>> s
<Series>
<Index>
Earth    1
Mars     2
Jupiter  67
Saturn   62
Uranus   27
Neptune  14
<<U7>    <int64>
>>> [k for k, v in s.items() if v > 60]
['Jupiter', 'Saturn']

#end_Series-items()


#start_Series-get()
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'), dtype=np.int64)
>>> [s.get(k, None) for k in ('Mercury', 'Neptune', 'Pluto')]
[None, 14, None]

#end_Series-get()


#start_Series-__len__()
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'), dtype=np.int64)
>>> len(s)
6

#end_Series-__len__()


#start_Series-__sub__()
>>> s = sf.Series.from_items((('Venus', 108.2), ('Earth', 149.6), ('Saturn', 1433.5)))
>>> s
<Series>
<Index>
Venus    108.2
Earth    149.6
Saturn   1433.5
<<U6>    <float64>

>>> abs(s - s['Earth'])
<Series>
<Index>
Venus    41.39999999999999
Earth    0.0
Saturn   1283.9
<<U6>    <float64>

#end_Series-__sub__()


#start_Series-__gt__()
>>> s = sf.Series.from_items((('Venus', 108.2), ('Earth', 149.6), ('Saturn', 1433.5)))
>>> s > s['Earth']
<Series>
<Index>
Venus    False
Earth    False
Saturn   True
<<U6>    <bool>

#end_Series-__gt__()


#start_Series-__truediv__()
>>> s = sf.Series.from_items((('Venus', 108.2), ('Earth', 149.6), ('Saturn', 1433.5)))

>>> s / s['Earth']
<Series>
<Index>
Venus    0.7232620320855615
Earth    1.0
Saturn   9.582219251336898
<<U6>    <float64>

#end_Series-__truediv__()


#start_Series-__mul__()
>>> s1 = sf.Series((1, 2), index=('Earth', 'Mars'))
>>> s2 = sf.Series((2, 0), index=('Mars', 'Mercury'))
>>> s1 * s2
<Series>
<Index>
Earth    nan
Mars     4.0
Mercury  nan
<<U7>    <float64>

#end_Series-__mul__()


#start_Series-__eq__()
>>> s1 = sf.Series((1, 2), index=('Earth', 'Mars'))
>>> s2 = sf.Series((2, 0), index=('Mars', 'Mercury'))

>>> s1 == s2
<Series>
<Index>
Earth    False
Mars     True
Mercury  False
<<U7>    <bool>

#end_Series-__eq__()


#start_Series-relabel()
>>> s = sf.Series((0, 62, 13), index=('Venus', 'Saturn', 'Neptune'), dtype=np.int64)

>>> s.relabel({'Venus': 'Mercury'})
<Series>
<Index>
Mercury  0
Saturn   62
Neptune  13
<<U7>    <int64>

>>> s.relabel(lambda x: x[:2].upper())
<Series>
<Index>
VE       0
SA       62
NE       13
<<U2>    <int64>

#end_Series-relabel()


#start_Series-reindex()
>>> s = sf.Series((0, 62, 13), index=('Venus', 'Saturn', 'Neptune'))

>>> s.reindex(('Venus', 'Earth', 'Mars', 'Neptune'))
<Series>
<Index>
Venus    0.0
Earth    nan
Mars     nan
Neptune  13.0
<<U7>    <float64>

#end_Series-reindex()


#start_Series-shape
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'), dtype=np.int64)
>>> s
<Series>
<Index>
Earth    1
Mars     2
Jupiter  67
Saturn   62
Uranus   27
Neptune  14
<<U7>    <int64>
>>> s.shape
(6,)

#end_Series-shape


#start_Series-ndim
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'), dtype=np.int64)
>>> s.ndim
1

#end_Series-ndim


#start_Series-size
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'), dtype=np.int64)
>>> s.size
6

#end_Series-size


#start_Series-nbytes
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'), dtype=np.int64)
>>> s.nbytes
48

#end_Series-nbytes


#start_Series-dtype
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'), dtype=np.int64)
>>> s.dtype
dtype('int64')

#end_Series-dtype


#start_Series-iter_element()
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'))
>>> [x for x in s.iter_element()]
[1, 2, 67, 62, 27, 14]

#end_Series-iter_element()


#start_Series-iter_element().apply()
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'))
>>> s.iter_element().apply(lambda v: v > 20)
<Series>
<Index>
Earth    False
Mars     False
Jupiter  True
Saturn   True
Uranus   True
Neptune  False
<<U7>    <bool>

#end_Series-iter_element().apply()


#start_Series-iter_element().apply_iter()
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'))
>>> [x for x in s.iter_element().apply_iter(lambda v: v > 20)]
[False, False, True, True, True, False]

#end_Series-iter_element().apply_iter()


#start_Series-iter_element_items()
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'))
>>> [x for x in s.iter_element_items()]
[('Earth', 1), ('Mars', 2), ('Jupiter', 67), ('Saturn', 62), ('Uranus', 27), ('Neptune', 14)]

#end_Series-iter_element_items()


#start_Series-iter_element_items().apply()
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'))
>>> s.iter_element_items().apply(lambda k, v: v if 'u' in k else None)
<Series>
<Index>
Earth    None
Mars     None
Jupiter  67
Saturn   62
Uranus   27
Neptune  14
<<U7>    <object>

#end_Series-iter_element_items().apply()


#start_Series-iter_element_items().apply_iter_items()
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'))

>>> [x for x in s.iter_element_items().apply_iter_items(lambda k, v: k.upper() if v > 20 else None)]
[('Earth', None), ('Mars', None), ('Jupiter', 'JUPITER'), ('Saturn', 'SATURN'), ('Uranus', 'URANUS'), ('Neptune', None)]


#end_Series-iter_element_items().apply_iter_items()


#start_Series-iter_group()
>>> s = sf.Series((0, 0, 1, 2), index=('Mercury', 'Venus', 'Earth', 'Mars'), dtype=np.int64)
>>> next(iter(s.iter_group()))
<Series>
<Index>
Mercury  0
Venus    0
<<U7>    <int64>
>>> [x.values.tolist() for x in s.iter_group()]
[[0, 0], [1], [2]]

#end_Series-iter_group()


#start_Series-iter_group_items()
>>> s = sf.Series((0, 0, 1, 2), index=('Mercury', 'Venus', 'Earth', 'Mars'))
>>> [(k, v.index.values.tolist()) for k, v in iter(s.iter_group_items()) if k > 0]
[(1, ['Earth']), (2, ['Mars'])]

#end_Series-iter_group_items()


#start_Series-assign[]()
>>> s = sf.Series.from_items((('Venus', 108.2), ('Earth', 149.6), ('Saturn', 1433.5)))
>>> s
<Series>
<Index>
Venus    108.2
Earth    149.6
Saturn   1433.5
<<U6>    <float64>
>>> s.assign['Earth'](150)
<Series>
<Index>
Venus    108.2
Earth    150.0
Saturn   1433.5
<<U6>    <float64>
>>> s.assign['Earth':](0)
<Series>
<Index>
Venus    108.2
Earth    0.0
Saturn   0.0
<<U6>    <float64>

#end_Series-assign[]()


#start_Series-assign.loc[]()
>>> s = sf.Series.from_items((('Venus', 108.2), ('Earth', 149.6), ('Saturn', 1433.5)))
>>> s.assign.loc[s < 150](0)
<Series>
<Index>
Venus    0.0
Earth    0.0
Saturn   1433.5
<<U6>    <float64>

#end_Series-assign.loc[]()


#start_Series-assign.iloc[]()
>>> s = sf.Series.from_items((('Venus', 108.2), ('Earth', 149.6), ('Saturn', 1433.5)))
>>> s.assign.iloc[-1](0)
<Series>
<Index>
Venus    108.2
Earth    149.6
Saturn   0.0
<<U6>    <float64>

#end_Series-assign.iloc[]()


#start_Series-drop[]
>>> s = sf.Series((0, 0, 1, 2), index=('Mercury', 'Venus', 'Earth', 'Mars'), dtype=np.int64)
>>> s
<Series>
<Index>
Mercury  0
Venus    0
Earth    1
Mars     2
<<U7>    <int64>
>>> s.drop[s < 1]
<Series>
<Index>
Earth    1
Mars     2
<<U7>    <int64>
>>> s.drop[['Mercury', 'Mars']]
<Series>
<Index>
Venus    0
Earth    1
<<U7>    <int64>

#end_Series-drop[]


#start_Series-drop.iloc[]
>>> s = sf.Series((0, 0, 1, 2), index=('Mercury', 'Venus', 'Earth', 'Mars'), dtype=np.int64)
>>> s.drop.iloc[-2:]
<Series>
<Index>
Mercury  0
Venus    0
<<U7>    <int64>

#end_Series-drop.iloc[]


#start_Series-[]
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'), dtype=np.int64)
>>> s
<Series>
<Index>
Earth    1
Mars     2
Jupiter  67
Saturn   62
Uranus   27
Neptune  14
<<U7>    <int64>

>>> s['Mars']
2
>>> s['Mars':]
<Series>
<Index>
Mars     2
Jupiter  67
Saturn   62
Uranus   27
Neptune  14
<<U7>    <int64>
>>> s[['Mars', 'Saturn']]
<Series>
<Index>
Mars     2
Saturn   62
<<U7>    <int64>
>>> s[s > 60]
<Series>
<Index>
Jupiter  67
Saturn   62
<<U7>    <int64>

#end_Series-[]


#start_Series-iloc[]
>>> s = sf.Series((1, 2, 67, 62, 27, 14), index=('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'), dtype=np.int64)
>>> s.iloc[-2:]
<Series>
<Index>
Uranus   27
Neptune  14
<<U7>    <int64>

#end_Series-iloc[]


#-------------------------------------------------------------------------------
# Frame


#start_Frame-from_dict()
>>> sf.Frame.from_dict(dict(diameter=(12756, 142984, 120536), mass=(5.97, 1898, 568)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64))
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Jupiter 142984   1898.0
Saturn  120536   568.0
<<U7>   <int64>  <float64>

#end_Frame-from_dict()


#start_FrameGO-from_dict()
>>> f = sf.FrameGO.from_dict(dict(diameter=(12756, 142984, 120536), mass=(5.97, 1898, 568)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64))
>>> f['radius'] = f['diameter'] * 0.5
>>> f
<FrameGO>
<IndexGO> diameter mass      radius    <<U8>
<Index>
Earth     12756    5.97      6378.0
Jupiter   142984   1898.0    71492.0
Saturn    120536   568.0     60268.0
<<U7>     <int64>  <float64> <float64>

#end_FrameGO-from_dict()


#start_Frame-from_records()
>>> index = ('Mercury', 'Venus', 'Earth', 'Mars')
>>> columns = ('diameter', 'gravity', 'temperature')
>>> records = ((4879, 3.7, 167), (12104, 8.9, 464), (12756, 9.8, 15), (6792, 3.7, -65))
>>> sf.Frame.from_records(records, index=index, columns=columns, dtypes=dict(diameter=np.int64, temperature=np.int64))
<Frame>
<Index> diameter gravity   temperature <<U11>
<Index>
Mercury 4879     3.7       167
Venus   12104    8.9       464
Earth   12756    9.8       15
Mars    6792     3.7       -65
<<U7>   <int64>  <float64> <int64>

#end_Frame-from_records()



#start_Frame-from_items()
>>> sf.Frame.from_items((('diameter', (12756, 142984, 120536)), ('mass', (5.97, 1898, 568))), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64))
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Jupiter 142984   1898.0
Saturn  120536   568.0
<<U7>   <int64>  <float64>

#end_Frame-from_items()



#start_Frame-from_concat()
>>> f1 = sf.Frame.from_dict(dict(diameter=(12756, 142984), mass=(5.97, 1898)), index=('Earth', 'Jupiter'))
>>> f2 = sf.Frame.from_dict(dict(mass=(0.642, 102), moons=(2, 14)), index=('Mars', 'Neptune'))
>>> sf.Frame.from_concat((f1, f2))
<Frame>
<Index> diameter  mass      moons     <<U8>
<Index>
Earth   12756.0   5.97      nan
Jupiter 142984.0  1898.0    nan
Mars    nan       0.642     2.0
Neptune nan       102.0     14.0
<<U7>   <float64> <float64> <float64>

>>> sf.Frame.from_concat((f1, f2), union=False)
<Frame>
<Index> mass      <<U8>
<Index>
Earth   5.97
Jupiter 1898.0
Mars    0.642
Neptune 102.0
<<U7>   <float64>

#end_Frame-from_concat()



#start_Frame-from_structured_array()
>>> a = np.array([('Venus', 4.87, 464), ('Neptune', 102, -200)], dtype=[('name', object), ('mass', 'f4'), ('temperature', 'i4')])
>>> sf.Frame.from_structured_array(a, index_depth=1)
<Frame>
<Index>  mass              temperature <<U11>
<Index>
Venus    4.869999885559082 464
Neptune  102.0             -200
<object> <float32>         <int32>

#end_Frame-from_structured_array()



#start_Frame-from_csv()
>>> from io import StringIO
>>> filelike = StringIO('name,mass,temperature\\nVenus,4.87,464\\nNeptune,102,-200')
>>> sf.Frame.from_csv(filelike, index_depth=1, dtypes=dict(temperature=np.int64))
<Frame>
<Index> mass      temperature <<U11>
<Index>
Venus   4.87      464
Neptune 102.0     -200
<<U7>   <float64> <int64>

#end_Frame-from_csv()



#start_Frame-items()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 142984, 120536), temperature=(15, -110, -140)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(temperature=np.int64, diameter=np.int64))
>>> f
<Frame>
<Index> diameter temperature <<U11>
<Index>
Earth   12756    15
Jupiter 142984   -110
Saturn  120536   -140
<<U7>   <int64>  <int64>
>>> len(f)
3
>>> [k for k, v in f.items() if (v < 0).any()]
['temperature']

#end_Frame-items()


#start_Frame-get()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 142984, 120536), temperature=(15, -110, -140)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(temperature=np.int64, diameter=np.int64))

>>> f.get('diameter')
<Series: diameter>
<Index>
Earth              12756
Jupiter            142984
Saturn             120536
<<U7>              <int64>

>>> f.get('mass', np.nan)
nan

#end_Frame-get()


#start_Frame-__contains__()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 142984, 120536), temperature=(15, -110, -140)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(temperature=np.int64, diameter=np.int64))

>>> 'temperature' in f
True

#end_Frame-__contains__()


#start_Frame-values
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 142984, 120536), temperature=(15, -110, -140)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(temperature=np.int64, diameter=np.int64))

>>> f.values.tolist()
[[12756, 15], [142984, -110], [120536, -140]]

#end_Frame-values


#start_Frame-__truediv__()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'), dtypes=dict(diameter=np.int64))
>>> f
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Mars    6792     0.642
Jupiter 142984   1898.0
<<U7>   <int64>  <float64>

>>> f / f.loc['Earth']
<Frame>
<Index> diameter           mass                <<U8>
<Index>
Earth   1.0                1.0
Mars    0.5324553151458138 0.10753768844221107
Jupiter 11.209156475384132 317.92294807370183
<<U7>   <float64>          <float64>

#end_Frame-__truediv__()


#start_Frame-max()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 142984, 120536), mass=(5.97, 1898, 568)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64))
>>> f
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Jupiter 142984   1898.0
Saturn  120536   568.0
<<U7>   <int64>  <float64>

>>> f.max()
<Series>
<Index>
diameter 142984.0
mass     1898.0
<<U8>    <float64>

#end_Frame-max()


#start_Frame-min()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 142984, 120536), mass=(5.97, 1898, 568)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64))

>>> f.min()
<Series>
<Index>
diameter 12756.0
mass     5.97
<<U8>    <float64>

#end_Frame-min()


#start_Frame-std()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 142984, 120536), mass=(5.97, 1898, 568)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64))

>>> f.std()
<Series>
<Index>
diameter 56842.64155250587
mass     793.344204533358
<<U8>    <float64>

#end_Frame-std()


#start_Frame-sum()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 142984, 120536), mass=(5.97, 1898, 568)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64))
>>> f
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Jupiter 142984   1898.0
Saturn  120536   568.0
<<U7>   <int64>  <float64>

>>> f.sum()
<Series>
<Index>
diameter 276276.0
mass     2471.9700000000003
<<U8>    <float64>

#end_Frame-sum()


#start_Frame-mean()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 142984, 120536), mass=(5.97, 1898, 568)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64))

>>> f.mean()
<Series>
<Index>
diameter 92092.0
mass     823.9900000000001
<<U8>    <float64>

#end_Frame-mean()


#start_Frame-relabel()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'), dtypes=dict(diameter=np.int64))

>>> f.relabel(index=lambda x: x[:2].upper(), columns={'mass': 'mass(1e24kg)'})
<Frame>
<Index> diameter mass(1e24kg) <<U12>
<Index>
EA      12756    5.97
MA      6792     0.642
JU      142984   1898.0
<<U2>   <int64>  <float64>

#end_Frame-relabel()


#start_Frame-reindex()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'), dtypes=dict(diameter=np.int64))
>>> f
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Mars    6792     0.642
Jupiter 142984   1898.0
<<U7>   <int64>  <float64>

>>> f.reindex(index=('Jupiter', 'Mars', 'Mercury'), columns=('density', 'mass'))
<Frame>
<Index> density   mass      <<U7>
<Index>
Jupiter nan       1898.0
Mars    nan       0.642
Mercury nan       nan
<<U7>   <float64> <float64>

#end_Frame-reindex()


#start_Frame-iter_element()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'), dtypes=dict(diameter=np.int64))

>>> [x for x in f.iter_element()]
[12756, 5.97, 6792, 0.642, 142984, 1898.0]

#end_Frame-iter_element()


#start_Frame-iter_element().apply()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'), dtypes=dict(diameter=np.int64))

>>> f.iter_element().apply(lambda x: x ** 2)
<Frame>
<Index> diameter    mass                <<U8>
<Index>
Earth   162715536   35.640899999999995
Mars    46131264    0.41216400000000003
Jupiter 20444424256 3602404.0
<<U7>   <object>    <object>

#end_Frame-iter_element().apply()


#start_Frame-iter_element_items()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'))

>>> [x for x in f.iter_element_items()]
[(('Earth', 'diameter'), 12756), (('Earth', 'mass'), 5.97), (('Mars', 'diameter'), 6792), (('Mars', 'mass'), 0.642), (('Jupiter', 'diameter'), 142984), (('Jupiter', 'mass'), 1898.0)]

#end_Frame-iter_element_items()


#start_Frame-iter_element_items().apply()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'))

>>> f.iter_element_items().apply(lambda k, v: v ** 2 if k[0] == 'Mars' else None)
<Frame>
<Index> diameter mass                <<U8>
<Index>
Earth   None     None
Mars    46131264 0.41216400000000003
Jupiter None     None
<<U7>   <object> <object>

#end_Frame-iter_element_items().apply()


#start_Frame-iter_array()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'), dtypes=dict(diameter=np.int64))
>>> f
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Mars    6792     0.642
Jupiter 142984   1898.0
<<U7>   <int64>  <float64>

>>> [x.tolist() for x in f.iter_array(axis=0)]
[[12756, 6792, 142984], [5.97, 0.642, 1898.0]]

>>> [x.tolist() for x in f.iter_array(axis=1)]
[[12756.0, 5.97], [6792.0, 0.642], [142984.0, 1898.0]]

#end_Frame-iter_array()


#start_Frame-iter_array().apply()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'), dtypes=dict(diameter=np.int64))
>>> f
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Mars    6792     0.642
Jupiter 142984   1898.0
<<U7>   <int64>  <float64>

>>> f.iter_array(axis=0).apply(np.sum)
<Series>
<Index>
diameter 162532.0
mass     1904.612
<<U8>    <float64>

#end_Frame-iter_array().apply()


#start_Frame-iter_array_items()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'))

>>> [x for x in f.iter_array_items(axis=0)]
[('diameter', array([ 12756,   6792, 142984])), ('mass', array([5.970e+00, 6.420e-01, 1.898e+03]))]

>>> [x for x in f.iter_array_items(axis=1)]
[('Earth', array([1.2756e+04, 5.9700e+00])), ('Mars', array([6.792e+03, 6.420e-01])), ('Jupiter', array([142984.,   1898.]))]

>>> f.iter_array_items(axis=1).apply(lambda k, v: v.sum() if k == 'Earth' else 0)
<Series>
<Index>
Earth    12761.97
Mars     0.0
Jupiter  0.0
<<U7>    <float64>

#end_Frame-iter_array_items()


#start_Frame-iter_array_items().apply()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'))

>>> f.iter_array_items(axis=1).apply(lambda k, v: v.sum() if k == 'Earth' else 0)
<Series>
<Index>
Earth    12761.97
Mars     0.0
Jupiter  0.0
<<U7>    <float64>

#end_Frame-iter_array_items().apply()


#start_Frame-iter_tuple()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'))

>>> [x for x in f.iter_tuple(axis=0)]
[Axis(Earth=12756, Mars=6792, Jupiter=142984), Axis(Earth=5.97, Mars=0.642, Jupiter=1898.0)]

>>> [x for x in f.iter_tuple(axis=1)]
[Axis(diameter=12756.0, mass=5.97), Axis(diameter=6792.0, mass=0.642), Axis(diameter=142984.0, mass=1898.0)]

#end_Frame-iter_tuple()


#start_Frame-iter_tuple().apply()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'))

>>> f.iter_tuple(axis=1).apply(lambda nt: nt.mass / (4 / 3 * np.pi * (nt.diameter * 0.5) ** 3))
<Series>
<Index>
Earth    5.49328558e-12
Mars     3.91330208e-12
Jupiter  1.24003876e-12
<<U7>    <float64>

#end_Frame-iter_tuple().apply()


#start_Frame-iter_tuple_items()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'))

>>> [x for x in f.iter_tuple_items(axis=0)]
[('diameter', Axis(Earth=12756, Mars=6792, Jupiter=142984)), ('mass', Axis(Earth=5.97, Mars=0.642, Jupiter=1898.0))]

>>> [x for x in f.iter_tuple_items(axis=1)]
[('Earth', Axis(diameter=12756.0, mass=5.97)), ('Mars', Axis(diameter=6792.0, mass=0.642)), ('Jupiter', Axis(diameter=142984.0, mass=1898.0))]

#end_Frame-iter_tuple_items()


#start_Frame-iter_tuple_items().apply()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'))

>>> f.iter_tuple_items(axis=1).apply(lambda k, v: v.diameter if k == 'Earth' else 0)
<Series>
<Index>
Earth    12756.0
Mars     0.0
Jupiter  0.0
<<U7>    <float64>

#end_Frame-iter_tuple_items().apply()


#start_Frame-iter_series()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'), dtypes=dict(diameter=np.int64))

>>> next(iter(f.iter_series(axis=0)))
<Series: diameter>
<Index>
Earth              12756
Mars               6792
Jupiter            142984
<<U7>              <int64>

>>> next(iter(f.iter_series(axis=1)))
<Series: Earth>
<Index>
diameter        12756.0
mass            5.97
<<U8>           <float64>

#end_Frame-iter_series()


#start_Frame-iter_series().apply()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'), dtypes=dict(diameter=np.int64))

>>> f.iter_series(axis=0).apply(lambda s: s.mean())
<Series>
<Index>
diameter 54177.333333333336
mass     634.8706666666667
<<U8>    <float64>

#end_Frame-iter_series().apply()


#start_Frame-iter_series_items()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'))

>>> [(k, v.mean()) for k, v in f.iter_series_items(axis=0)]
[('diameter', 54177.333333333336), ('mass', 634.8706666666667)]

>>> [(k, v.max()) for k, v in f.iter_series_items(axis=1)]
[('Earth', 12756.0), ('Mars', 6792.0), ('Jupiter', 142984.0)]

>>> f.iter_series_items(axis=0).apply(lambda k, v: v.mean() if k == 'diameter' else v.sum())
<Series>
<Index>
diameter 54177.333333333336
mass     1904.612
<<U8>    <float64>

#end_Frame-iter_series_items()


#start_Frame-iter_group()
>>> f = sf.Frame.from_dict(dict(mass=(0.33, 4.87, 5.97, 0.642), moons=(0, 0, 1, 2)), index=('Mercury', 'Venus', 'Earth', 'Mars'), dtypes=dict(moons=np.int64))
>>> next(iter(f.iter_group('moons')))
<Frame>
<Index> mass      moons   <<U5>
<Index>
Mercury 0.33      0
Venus   4.87      0
<<U7>   <float64> <int64>
>>> [x.shape for x in f.iter_group('moons')]
[(2, 2), (1, 2), (1, 2)]

#end_Frame-iter_group()


#start_Frame-iter_group_items()
>>> f = sf.Frame.from_dict(dict(mass=(0.33, 4.87, 5.97, 0.642), moons=(0, 0, 1, 2)), index=('Mercury', 'Venus', 'Earth', 'Mars'))
>>> [(k, v.index.values.tolist(), v['mass'].mean()) for k, v in f.iter_group_items('moons')]
[(0, ['Mercury', 'Venus'], 2.6), (1, ['Earth'], 5.97), (2, ['Mars'], 0.642)]

#end_Frame-iter_group_items()



#start_Frame-assign[]()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'), dtypes=dict(diameter=np.int64))
>>> f
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Mars    6792     0.642
Jupiter 142984   1898.0
<<U7>   <int64>  <float64>

>>> f.assign['mass'](f['mass'] * .001)
<Frame>
<Index> diameter mass               <<U8>
<Index>
Earth   12756    0.00597
Mars    6792     0.000642
Jupiter 142984   1.8980000000000001
<<U7>   <int64>  <float64>

#end_Frame-assign[]()


#start_Frame-assign.loc[]()
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 6792, 142984), mass=(5.97, 0.642, 1898)), index=('Earth', 'Mars', 'Jupiter'), dtypes=dict(diameter=np.int64))

>>> f.assign.loc['Mars', 'mass'](0)
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Mars    6792     0.0
Jupiter 142984   1898.0
<<U7>   <int64>  <float64>

>>> f.assign.loc['Mars':, 'diameter'](0)
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Mars    0        0.642
Jupiter 0        1898.0
<<U7>   <int64>  <float64>

>>> f.assign.loc[f['diameter'] > 10000, 'mass'](0)
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    0.0
Mars    6792     0.642
Jupiter 142984   0.0
<<U7>   <int64>  <float64>

#end_Frame-assign.loc[]()


#start_Frame-drop[]
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 142984, 120536), temperature=(15, -110, -140)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64, temperature=np.int64))

>>> f
<Frame>
<Index> diameter temperature <<U11>
<Index>
Earth   12756    15
Jupiter 142984   -110
Saturn  120536   -140
<<U7>   <int64>  <int64>

>>> f.drop['diameter']
<Frame>
<Index> temperature <<U11>
<Index>
Earth   15
Jupiter -110
Saturn  -140
<<U7>   <int64>

#end_Frame-drop[]


#start_Frame-drop.loc[]
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 142984, 120536), temperature=(15, -110, -140)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64, temperature=np.int64))
>>> f
<Frame>
<Index> diameter temperature <<U11>
<Index>
Earth   12756    15
Jupiter 142984   -110
Saturn  120536   -140
<<U7>   <int64>  <int64>

>>> f.drop.loc[f['temperature'] < 0]
<Frame>
<Index> diameter temperature <<U11>
<Index>
Earth   12756    15
<<U7>   <int64>  <int64>

#end_Frame-drop.loc[]


#start_Frame-drop.iloc[]
>>> f = sf.Frame.from_dict(dict(diameter=(12756, 142984, 120536), temperature=(15, -110, -140)), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64, temperature=np.int64))
>>> f
<Frame>
<Index> diameter temperature <<U11>
<Index>
Earth   12756    15
Jupiter 142984   -110
Saturn  120536   -140
<<U7>   <int64>  <int64>

>>> f.drop.iloc[-1, -1]
<Frame>
<Index> diameter <<U11>
<Index>
Earth   12756
Jupiter 142984
<<U7>   <int64>

#end_Frame-drop.iloc[]


#start_Frame-shape
>>> f = sf.Frame.from_items((('diameter', (12756, 142984, 120536)), ('mass', (5.97, 1898, 568))), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64))

>>> f
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Jupiter 142984   1898.0
Saturn  120536   568.0
<<U7>   <int64>  <float64>

>>> f.shape
(3, 2)

#end_Frame-shape


#start_Frame-ndim
>>> f = sf.Frame.from_items((('diameter', (12756, 142984, 120536)), ('mass', (5.97, 1898, 568))), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64))
>>> f
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Jupiter 142984   1898.0
Saturn  120536   568.0
<<U7>   <int64>  <float64>

>>> f.ndim
2

#end_Frame-ndim


#start_Frame-size
>>> f = sf.Frame.from_items((('diameter', (12756, 142984, 120536)), ('mass', (5.97, 1898, 568))), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64))
>>> f
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Jupiter 142984   1898.0
Saturn  120536   568.0
<<U7>   <int64>  <float64>

>>> f.size
6

#end_Frame-size


#start_Frame-nbytes
>>> f = sf.Frame.from_items((('diameter', (12756, 142984, 120536)), ('mass', (5.97, 1898, 568))), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64))
>>> f
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Jupiter 142984   1898.0
Saturn  120536   568.0
<<U7>   <int64>  <float64>

>>> f.nbytes
48

#end_Frame-nbytes


#start_Frame-dtypes
>>> f = sf.Frame.from_items((('diameter', (12756, 142984, 120536)), ('mass', (5.97, 1898, 568))), index=('Earth', 'Jupiter', 'Saturn'), dtypes=dict(diameter=np.int64))

>>> f
<Frame>
<Index> diameter mass      <<U8>
<Index>
Earth   12756    5.97
Jupiter 142984   1898.0
Saturn  120536   568.0
<<U7>   <int64>  <float64>

>>> f.dtypes
<Series>
<Index>
diameter int64
mass     float64
<<U8>    <object>

#end_Frame-dtypes


#start_Frame-[]
>>> index = ('Mercury', 'Venus', 'Earth', 'Mars')
>>> columns = ('diameter', 'gravity', 'temperature')
>>> records = ((4879, 3.7, 167), (12104, 8.9, 464), (12756, 9.8, 15), (6792, 3.7, -65))
>>> f = sf.Frame.from_records(records, index=index, columns=columns, dtypes=dict(diameter=np.int64, temperature=np.int64))
>>> f
<Frame>
<Index> diameter gravity   temperature <<U11>
<Index>
Mercury 4879     3.7       167
Venus   12104    8.9       464
Earth   12756    9.8       15
Mars    6792     3.7       -65
<<U7>   <int64>  <float64> <int64>

>>> f['gravity']
<Series: gravity>
<Index>
Mercury           3.7
Venus             8.9
Earth             9.8
Mars              3.7
<<U7>             <float64>
>>> f['gravity':]
<Frame>
<Index> gravity   temperature <<U11>
<Index>
Mercury 3.7       167
Venus   8.9       464
Earth   9.8       15
Mars    3.7       -65
<<U7>   <float64> <int64>
>>> f[['diameter', 'temperature']]
<Frame>
<Index> diameter temperature <<U11>
<Index>
Mercury 4879     167
Venus   12104    464
Earth   12756    15
Mars    6792     -65
<<U7>   <int64>  <int64>

#end_Frame-[]


#start_Frame-loc[]
>>> index = ('Mercury', 'Venus', 'Earth', 'Mars')
>>> columns = ('diameter', 'gravity', 'temperature')
>>> records = ((4879, 3.7, 167), (12104, 8.9, 464), (12756, 9.8, 15), (6792, 3.7, -65))
>>> f = sf.Frame.from_records(records, index=index, columns=columns, dtypes=dict(diameter=np.int64, temperature=np.int64))
>>> f
<Frame>
<Index> diameter gravity   temperature <<U11>
<Index>
Mercury 4879     3.7       167
Venus   12104    8.9       464
Earth   12756    9.8       15
Mars    6792     3.7       -65
<<U7>   <int64>  <float64> <int64>

>>> f.loc['Earth', 'temperature']
15
>>> f.loc['Earth':, 'temperature']
<Series: temperature>
<Index>
Earth                 15
Mars                  -65
<<U7>                 <int64>
>>> f.loc[f['temperature'] > 100, 'diameter']
<Series: diameter>
<Index>
Mercury            4879
Venus              12104
<<U7>              <int64>
>>> f.loc[sf.ILoc[-1], ['gravity', 'temperature']]
<Series: Mars>
<Index>
gravity        3.7
temperature    -65.0
<<U11>         <float64>

#end_Frame-loc[]


#start_Frame-iloc[]
>>> index = ('Mercury', 'Venus', 'Earth', 'Mars')
>>> columns = ('diameter', 'gravity', 'temperature')
>>> records = ((4879, 3.7, 167), (12104, 8.9, 464), (12756, 9.8, 15), (6792, 3.7, -65))
>>> f = sf.Frame.from_records(records, index=index, columns=columns, dtypes=dict(diameter=np.int64, temperature=np.int64))
>>> f
<Frame>
<Index> diameter gravity   temperature <<U11>
<Index>
Mercury 4879     3.7       167
Venus   12104    8.9       464
Earth   12756    9.8       15
Mars    6792     3.7       -65
<<U7>   <int64>  <float64> <int64>

>>> f.iloc[-2:, -1]
<Series: temperature>
<Index>
Earth                 15
Mars                  -65
<<U7>                 <int64>

#end_Frame-iloc[]




#-------------------------------------------------------------------------------
# index

#start_Index-__init__()
>>> sf.Index(('Mercury', 'Mars'), dtype=object)
<Index>
Mercury
Mars
<object>

>>> sf.Index(name[:2].upper() for name in ('Mercury', 'Mars'))
<Index>
ME
MA
<<U2>

#end_Index-__init__()


#start_IndexGO-append()
>>> a = sf.IndexGO(('Uranus', 'Neptune'))
>>> a.append('Pluto')
>>> a
<IndexGO>
Uranus
Neptune
Pluto
<<U7>

#end_IndexGO-append()


#start_Index-relabel()
>>> index = sf.Index(('Venus', 'Saturn', 'Neptune'))
>>> index.relabel({'Venus': 'Mars'})
<Index>
Mars
Saturn
Neptune
<<U7>

>>> index = sf.Index(('Venus', 'Saturn', 'Neptune'))
>>> index.relabel({'Neptune': 'Uranus'})
<Index>
Venus
Saturn
Uranus
<<U6>

>>> index.relabel(lambda x: x[:2].upper())
<Index>
VE
SA
NE
<<U2>

#end_Index-relabel()



#-------------------------------------------------------------------------------
# restore initial configuration
>>> sf.DisplayActive.set(_display_config_active)


'''


from static_frame.test.test_case import TestCase


class TestUnit(doctest.DocTestCase, TestCase):

    @staticmethod
    def get_readme_fp() -> str:

        target_fn = 'README.rst'

        fp = os.path.join(os.getcwd(), __file__)
        if not os.path.exists(fp):
            raise RuntimeError('got bad module path', fp)

        while len(fp) > len(os.sep):
            fp = os.path.dirname(fp)
            if target_fn in os.listdir(fp):
                return os.path.join(fp, target_fn)

        raise RuntimeError('could not find target fn', target_fn)

    @classmethod
    def get_readme_str(cls) -> str:
        # mutate the README
        fp_alt = cls.get_test_input('jph_photos.txt')

        readme_fp = cls.get_readme_fp()
        with open(readme_fp) as f:
            readme_str = f.read()

        # update display config to remove colors
        readme_str = '''
>>> _display_config = sf.DisplayActive.get()
>>> sf.DisplayActive.update(type_color=False)
>>>
        ''' + readme_str

        # inject content from local files
        src = ">>> frame = sf.Frame.from_json_url('https://jsonplaceholder.typicode.com/photos', dtypes=dict(albumId=np.int64, id=np.int64))"

        # using a raw string to avoid unicode decoding issues on windows
        dst = ">>> frame = sf.Frame.from_tsv(r'%s', dtypes=dict(albumId=np.int64, id=np.int64), encoding='utf-8')" % fp_alt

        if src not in readme_str:
            raise RuntimeError('did not find expected string')

        readme_str = readme_str.replace(src, dst)

        # restore active config
        readme_str = readme_str + '''
>>> sf.DisplayActive.set(_display_config)
        '''

        return readme_str

    @staticmethod
    def update_readme(source: object) -> None:
        target = "sf.Frame.from_json_url('https://jsonplaceholder.typicode.com/photos')"


    def __init__(self, *args: tp.Any, **kwargs: tp.Any) -> None:

        doctest_str = '\n'.join((api_example_str, self.get_readme_str()))

        sample = doctest.DocTestParser().get_doctest(
                doctest_str,
                globs={},
                name='test_doc',
                filename=None,
                lineno=None)

        super().__init__(sample, **kwargs)


if __name__ == "__main__":
    import unittest
    unittest.main()





# UNUSED


# #start_Frame-from_records()
# >>> sf.Frame.from_records(((-65, 227.9), (-200, 4495.1)), columns=('temperature', 'distance'), index=('Mars', 'Neptune'), dtypes=dict(temperature=np.int64))
# <Frame>
# <Index> temperature distance  <<U11>
# <Index>
# Mars    -65         227.9
# Neptune -200        4495.1
# <<U7>   <int64>     <float64>
# #end_Frame-from_records()
