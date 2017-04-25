/**
 *
 * @license
 * Copyright (C) 2016 Joseph Roque
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * @author Joseph Roque
 * @file index.js
 * @description Exports files in this directory
 *
 * @flow
 */
'use strict';

module.exports = [
  {
    name: '/disciplines.json',
    require: require ('./json/disciplines.json'),
    schema: require('./json/__schemas__/disciplines.schema.json'),
  },
  {
    name: '/discover.json',
    require: require ('./json/discover.json'),
    schema: require('./json/__schemas__/discover.schema.json'),
  },
  {
    name: '/faculties.json',
    require: require ('./json/faculties.json'),
    schema: require('./json/__schemas__/faculties.schema.json'),
  },
  {
    name: '/lecture_formats.json',
    require: require ('./json/lecture_formats.json'),
    schema: require('./json/__schemas__/lecture_formats.schema.json'),
  },
  {
    name: '/room_types.json',
    require: require ('./json/room_types.json'),
    schema: require('./json/__schemas__/room_types.schema.json'),
  },
  {
    name: '/settings.json',
    require: require ('./json/settings.json'),
    schema: require('./json/__schemas__/settings.schema.json'),
  },
  {
    name: '/shuttle.json',
    require: require ('./json/shuttle.json'),
    schema: require('./json/__schemas__/shuttle.schema.json'),
  },
  {
    name: '/study_spots.json',
    require: require ('./json/study_spots.json'),
    schema: require('./json/__schemas__/study_spots.schema.json'),
  },
  {
    name: '/transit.json',
    require: require ('./json/transit.json'),
    schema: require('./json/__schemas__/transit.schema.json'),
  },
  {
    name: '/translations.en.json',
    require: require ('./json/translations.en.json'),
    schema: require('./json/__schemas__/translations.schema.json'),
  },
  {
    name: '/translations.fr.json',
    require: require ('./json/translations.fr.json'),
    schema: require('./json/__schemas__/translations.schema.json'),
  },
  {
    name: '/university.fr.json',
    require: require ('./json/university.json'),
    schema: require('./json/__schemas__/university.schema.json'),
  },
  {
    name: '/useful_links.fr.json',
    require: require ('./json/useful_links.json'),
    schema: require('./json/__schemas__/useful_links.schema.json'),
  },
];
