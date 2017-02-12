'''
The Pitt API, to access workable data of the University of Pittsburgh
Copyright (C) 2015 Ritwik Gupta

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''
import unittest

import timeout_decorator

from PittAPI import course
from . import PittServerError

TERM = '2177'


class CourseTest(unittest.TestCase):
    @timeout_decorator.timeout(30, timeout_exception=PittServerError)
    def test_get_courses(self):
        self.assertIsInstance(course.get_courses(TERM, 'CS'), list)

    @timeout_decorator.timeout(60, timeout_exception=PittServerError)
    def test_get_courses_subject_query(self):
        self.assertIsInstance(course.get_courses(TERM, 'BIOSC'), list)

    @timeout_decorator.timeout(60, timeout_exception=PittServerError)
    def test_get_courses_programs_query(self):
        self.assertIsInstance(course.get_courses(TERM, 'CLST'), list)

    @timeout_decorator.timeout(60, timeout_exception=PittServerError)
    def test_get_courses_off_campus_query(self):
        self.assertIsInstance(course.get_courses(TERM, 'BCCC'), list)

    @timeout_decorator.timeout(30, timeout_exception=PittServerError)
    def test_get_courses_by_req(self):
        self.assertIsInstance(course.get_courses_by_req(TERM, 'Q'), list)

    @timeout_decorator.timeout(30, timeout_exception=PittServerError)
    def test_get_class_description(self):
        self.assertIsInstance(course.get_class_description(TERM, '10045'), str)

    @timeout_decorator.timeout(30, timeout_exception=PittServerError)
    def test_invalid_subject(self):
        test_subjects =['AAA', 'BBB', 'CCC']
        for subject in test_subjects:
            self.assertRaises(ValueError, course.get_courses, TERM, subject)
