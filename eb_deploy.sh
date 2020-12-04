#!/bin/bash
echo "cd eb-app"
cd eb-app
echo "eb deploy"
eb deploy
echo "cd .."
cd ..
