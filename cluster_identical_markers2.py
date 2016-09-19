#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  cluster_identical_markers.py
#  
#  Copyright 2016 Junli Zhang <zhjl86@gmail.com>
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
dd = dict()
nn = dict()
with open("zzd_identical_snps.txt") as f:
	for line in f:
		snp1, snp2 = line.rstrip().split("\t")
		if snp1 not in dd:
			dd[snp1] = (snp1,snp2)
			nn[snp1] = 1
		else:
			dd[snp1] = dd[snp1] + (snp2,)
			nn[snp1] += 1

#def myprint(k,d):
	#v = d[k]
	##dum[k] = 1
	#print k,
	#if v in d:
		#myprint(v,d)
	#else:
		#print v

##myprint("1", dd)
##print dum
##for kk in sorted(dd2, key=dd2.get, reverse=True): # sort based on group number
#for kk in dd:
	##if kk not in dum and kk not in dd.values():
	#if kk not in dd.values():
          #myprint(kk,dd)

# sort value length
# the longest value should contact all the snps for each group
vv = ()
for kk in sorted(dd, key=lambda k: len(dd[k]), reverse=True):
	#if set(dd[kk]) < set(vv):
	if kk in vv:
		continue
	else:
		print ",".join(dd[kk])
		vv = dd[kk] + vv
