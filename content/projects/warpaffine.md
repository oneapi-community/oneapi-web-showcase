---
title: "Warpaffine"
date: 2024-06-23T15:11:37-07:00
draft: false
githublink: https://github.com/ZEISS/warpaffine
tags: ['tbb', 'image-processing']
category:  ['image-processing']
---

This is an experimental effort at implementing a "Deskew operation" with the best performance possible.

With an acquisition from a [Lattice Lightsheet microscope](https://www.zeiss.com/microscopy/en/products/light-microscopes/light-sheet-microscopes/lattice-lightsheet-7.html) the image slices are created at a skewed angle. In order to create a regular volumetric image in Cartesian coordinates, the volume needs to undergo a geometric transformation (and affine transformation, hence the name of this project) and needs to be resampled.
