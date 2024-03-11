#!/bin/bash

# Simulate a segmentation fault
echo "Simulating segmentation fault..."
kill -SEGV $$
