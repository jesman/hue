#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('rdbms.views',
  url(r'^$', 'index', name='index'),
  url(r'^execute/(?P<design_id>\d+)?$', 'execute_query', name='execute_query'),
  url(r'^results/(?P<id>\d+)/(?P<first_row>\d+)$', 'view_results', name='view_results'),
)

urlpatterns += patterns('beeswax.views',
  url(r'^autocomplete/$', 'autocomplete', name='autocomplete'),
  url(r'^autocomplete/(?P<database>\w+)/$', 'autocomplete', name='autocomplete'),
  url(r'^autocomplete/(?P<database>\w+)/(?P<table>\w+)$', 'autocomplete', name='autocomplete'),

  url(r'^save_design_properties$', 'save_design_properties', name='save_design_properties'), # Ajax

  url(r'^my_queries$', 'my_queries', name='my_queries'),
  url(r'^list_designs$', 'list_designs', name='list_designs'),
  url(r'^list_trashed_designs$', 'list_trashed_designs', name='list_trashed_designs'),
  url(r'^delete_designs$', 'delete_design', name='delete_design'),
  url(r'^restore_designs$', 'restore_design', name='restore_design'),
  url(r'^clone_design/(?P<design_id>\d+)$', 'clone_design', name='clone_design'),
  url(r'^query_history$', 'list_query_history', name='list_query_history')
)
