#!/bin/bash

rm -rf docs
cp -r _build/html docs
cp docs_config.yml docs/_config_yml

