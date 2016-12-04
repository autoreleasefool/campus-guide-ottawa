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
 * @file TransitCampuses.js
 * @description Details about the campuses that offer transit stations.
 *
 */
'use strict';

/* eslint-disable global-require */

// Imports
import * as Constants from 'Constants';

module.exports = [
  {
    background: Constants.Colors.transparentGarnet,
    image: require('../images/placeholders/outer_placeholder.jpg'),
    name_en: 'Main Campus',
    name_fr: 'Campus principal',
  },
  {
    background: Constants.Colors.transparentCharcoalGrey,
    image: require('../images/placeholders/outer_placeholder.jpg'),
    name: 'Lees',
  },
  {
    background: Constants.Colors.transparentLightGrey,
    image: require('../images/placeholders/outer_placeholder.jpg'),
    name: 'RGN',
  },
  {
    background: Constants.Colors.transparentDarkGrey,
    image: require('../images/placeholders/outer_placeholder.jpg'),
    name: 'MBA',
  },
];
