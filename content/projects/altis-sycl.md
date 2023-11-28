---
title: "Altis Sycl"
date: 2023-11-14T12:51:11-08:00
draft: false
githublink: https://github.com/esa-tu-darmstadt/altis_sycl
tags: ['benchmark', 'sycl']
---

Altis-SYCL is a SYCL-based implementation of the Altis GPGPU benchmark
suite (originally written in CUDA) for CPUs, GPUs, and FPGAs.

Altis-SYCL has been migrated from CUDA using the DPC++ Compatibility Tool
(DPCT) of oneAPI v2022.1. Our main focus is to evaluate the performance
of these GPU-tailored SYCL kernels and to investigate their optimization
potential for FPGAs. For some cases, minor code changes were made to
speedup the FPGA port as our interest lies in the achievable performance
without major rework of the kernels.

The benchmarks.md file contains a portion of our performance evaluation
on various accelerators.
