# -*- coding: utf-8 -*-
'''
Created on 2018年1月29日

@author: Jeff Yang
'''


def find_start_with_test(filename):
    """查找以Test开头的字符串"""
    with open(filename) as f:
        for line in f:
            if line.startswith('Test'):
                print(line.strip())


def find_start_and_end_with_test(filename):
    """查找以Test开头且以Test结尾的字符串"""
    with open(filename) as f:
        for line in f:
            # 结尾是换行符，所以要[:-1]去除最后的字符，或者匹配'Test\n'
            if line.startswith('Test') and line[:-1].endswith('Test'):
                print(line.strip())


def check_legal_variable_name(name):
    """检查是否是下划线或小写字母开头的合法变量名"""
    print(name and (name[0] == '_' or 'a' <= name[0] <= 'z'))


# find_start_with_test('test.txt')
find_start_and_end_with_test('test.txt')
check_legal_variable_name('_value1')
check_legal_variable_name('3_value1')