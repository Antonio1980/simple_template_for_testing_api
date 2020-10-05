#!/bin/bash

if [[ ! -d ~/Allure/bin/ ]]; then
  # shellcheck disable=SC2242
  exit "You should install Allure locally first."
fi

~/Allure/bin/allure generate ../allure_/allure_results/ -o ../allure_/allure_reports/ --clean
cp -r ../allure_/allure_reports/history ../allure_/allure_results/history
~/Allure/bin/allure generate ../allure_/allure_results/ -o ../allure_/allure_reports/ --clean
