#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Dictionary.py
#  
#  Copyright 2017 Derek <Derek@D-UNIT>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



#dictionary = {key:value}
alien_0 = {'points':5}

#just creating some variables with a condition
if alien_0:
	arms=5
	legs=3
	attributes=['warts', 'puss', 'fungus', str(arms)+' arms',
		str(legs)+' legs']

#appending the dictionary ['key']=value
alien_0['appendages']=arms+legs
alien_0['attributes']=attributes
alien_0['color']='green'
print(alien_0['color'])
alien_0['blowme']=0
alien_0['harder']=3
alien_0['color']='yellow'

#deleting keys
del alien_0['blowme']
del alien_0['harder']

#show your work
print(alien_0['color'])
print(alien_0['points'])
for key, value in alien_0.items():
	value = str(value)
	print("\nKey: " + key)
	print("Value: " + value)
print('\n')
for key, value in alien_0.items():
	value = str(value)
	print("\nKey: " + key)
	print("Value: " + value)
print('\n')
for attribute in alien_0['attributes']:
	print(attribute)
del alien_0['attributes']
for key in set(alien_0.values()):
	print (key)
