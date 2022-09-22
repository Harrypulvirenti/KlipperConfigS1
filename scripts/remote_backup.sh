#!/bin/bash
git -C ~/klipper_config pull
git -C ~/klipper_config add .
git -C ~/klipper_config commit -m "`date`"
git -C ~/klipper_config push
