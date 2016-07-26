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
 * @file DiscoverSections.js
 * @description Provides information about the possible sections that can be selected in the "Discover" screen.
 *
 */
'use strict';

/* eslint-disable global-require */

module.exports = [
  {
    id: 'pop',
    name_en: 'Popular Destinations',
    name_fr: 'Les destinations populaires',
    image: require('../images/buildings/outer_placeholder.jpg'),
    icon: {
      android: {
        name: 'whatshot',
        class: 'material',
      },
      ios: {
        name: 'ios-flame',
        class: 'ionicon',
      },
    },
  },
  {
    id: 'stu',
    name_en: 'Study Spots',
    name_fr: 'Taches d\'études',
    image: require('../images/buildings/outer_placeholder.jpg'),
    icon: {
      android: {
        name: 'local-library',
        class: 'material',
      },
      ios: {
        name: 'ios-book',
        class: 'ionicon',
      },
    },
  },
  {
    id: 'use',
    name_en: 'Useful Links',
    name_fr: 'Liens utiles',
    image: require('../images/buildings/outer_placeholder.jpg'),
    icon: {
      name: 'insert-link',
      class: 'material',
    },
  },
  {
    id: 'bus',
    name: 'OC Transpo',
    image: require('../images/buildings/outer_placeholder.jpg'),
    icon: {
      name: 'directions-bus',
      class: 'material',
    },
  },
  {
    id: 'shu',
    name_en: 'Shuttle',
    name_fr: 'La navette',
    image: require('../images/buildings/outer_placeholder.jpg'),
    icon: {
      name: 'local-shipping',
      class: 'material',
    },
  },
];
