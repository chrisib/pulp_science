#!/usr/bin/env python
"""
This script is a re-implementation of Polyhedron Magazine's original Pulp Heroes
random scientific invention name table, by David Noonan.  This can be found in
Dungeon Magazine #90/Polyhedron #149 from January 2002.
"""

import random

# the prefixes that can be prepended to other elements
PREFIX = [
  'Incini-',
  'Nova-',
  'Auto-',
  'Micro-',
  'Neo-',
  'Aero-',
  'Cryo-',
  'Nega-',
  'Multi-',
  'Electro-',
  'Hydro-',
  'Infini-',
  'Magneto-',
  'Omni-',
  'Porta-',
  'Mega-',
  'Uni-',
  'Hyper-',
  'Nano-',
  'Anti-'
]

# First catalyst
CATALYST_1 = [
  'Gaussian',
  'Zortillium',
  'Mu-Particle',
  'Microwave',
  'Infrared',
  'Ultraviolet',
  'Full-Spectrum',
  'Polarity',
  'Dark Matter',
  'Positron',
  'Gamma-Ray',
  'Neutron',
  'Electron',
  'Atomic',
  'Kirlian',
  'Jet',
  'Martellium',
  'Space',
  'Inertial',
  'Quantum'
]

# Second catalyst
CATALYST_2 = [
  'Wave',
  'Particle',
  'Beam',
  'Field',
  'Alloy',
  'Vector',
  'Plasma',
  'Pulse',
  'Radiation',
  'Flux',
  'Reaction',
  'Vapor',
  'Element',
  'Molecule',
  'Atom',
  'Spectrum',
  'Phase',
  'Laser',
  'Ray',
  'Force'
]

# First function
FUNCTION_1 = [
  'Converter',
  'Transformer',
  'Launcher',
  'Spectralyzer',
  'Capacitor',
  'Reflector',
  'Focus',
  'Enhancer',
  'Charger',
  'Targeter',
  'Emitter',
  'Transmitter',
  'Transporter',
  'Energy',
  'Matter',
  'Prismator',
  'Reactor',
  'Reverser',
  'Negator',
  'Neutralizer'
]

# Second function
FUNCTION_2 = [
  'Gun',
  'Sphere',
  'Unit',
  'Machine',
  'Array',
  'Rocket',
  'Compound',
  'Antenna',
  'Engine',
  'Drive',
  'Network',
  'Weapon',
  'Probe',
  'Robot',
  'Craft',
  'Bomb',
  'Suit',
  'Armor',
  'Shield',
  'Construct'	
]

ALL_COMPONENTS = [
  PREFIX,
  CATALYST_1,
  CATALYST_2,
  FUNCTION_1,
  FUNCTION_2
]

# the 8 possible orders of components
# -1 indicates not-used
# 0-4 indicates the order that the element appears in the final name
# e.g. index 2 would yeild C1 P F1: "Gaussian Incini-wave"
NAMES = [
#   Pre   C1     C2    F1     F2
  [ -1,    0,    -1,    1,    -1 ],
  [ -1,    0,     1,    2,    -1 ],
  [  1,    0,    -1,    2,    -1 ],
  [  0,   -1,     1,   -1,     2 ],
  [  1,    0,    -1,    2,     3 ],
  [  3,    0,     1,    2,     4 ],
  [ -1,    0,     1,    2,     3 ],
  [  1,    0,     2,    3,     4 ]
]

if __name__ == '__main__':
  name_format = random.choice(NAMES)
  name_parts = {}
  # go through the selected item from NAMES, choosing random items from each sub-list in ALL_COMPONENTS
  for part_index in range(len(name_format)):
    part = name_format[part_index]
    if part >= 0:
      next_part = random.choice(ALL_COMPONENTS[part_index])
      name_parts[part] = next_part

  name = ''
  # keys is conveniently already sorted, so we can just walk through it
  for part in name_parts.keys():
    name = name + name_parts[part]
    if name[-1] != '-':  # don't put a space after a prefix: it has a hyphen instead!
      name = name + ' '
  name = name.strip()    # remove the trailing space
  print(name)
