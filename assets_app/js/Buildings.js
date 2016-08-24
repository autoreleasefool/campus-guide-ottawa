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
 * @file Buildings.js
 * @description Provides names and images of all buildings on the University of Ottawa campus.
 *
 */
'use strict';

/* eslint-disable global-require */

module.exports = require('./BuildingsTemp');

// [
//   {
//     code: '3',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//     name: '3',
//     lat: 45.4230938,
//     long: -75.6832885,
//     facilities: [
//       'atm',
//       'food',
//       'printer',
//       'store',
//       'bed',
//       'alcohol',
//       'laundry',
//       'library',
//       'parking',
//       'mail',
//       'pharmacy',
//       'gym',
//       'pool',
//     ],
//     rooms: [
//       {
//         name: 'STE A0101',
//         type: 0,
//       },
//       {
//         name: 'STE B0102',
//         type: 1,
//       },
//       {
//         name: 'STE C0103',
//         type: 2,
//       },
//       {
//         name: 'STE E0104',
//         type: 3,
//       },
//       {
//         name: 'STE F0104',
//         type: 3,
//       },
//       {
//         name: 'STE G0104',
//         type: 3,
//       },
//       {
//         name: 'STE H0104',
//         type: 3,
//       },
//       {
//         name: 'STE I0104',
//         type: 3,
//       },
//       {
//         name: 'STE J0104',
//         type: 3,
//       },
//       {
//         name: 'STE K0104',
//         type: 3,
//       },
//       {
//         name: 'STE L0104',
//         type: 3,
//       },
//       {
//         name: 'STE M0104',
//         type: 3,
//       },
//       {
//         name: 'STE N0104',
//         type: 3,
//       },
//       {
//         name: 'STE O0104',
//         type: 3,
//       },
//     ],
//   },
//   {
//     code: '55',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: '56',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: '164',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: '226',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: '227',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: '242',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: '243',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: '244',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: '275',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'ARC',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'ART',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'ATK',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'AWHC',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'BRS',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'BSC',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'CBE',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'CBY',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'CRG',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'CTE',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'DMS',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'DRO',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'EMBA',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'FSS',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'FTX',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'GNN',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'GSD',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'HGN',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'HSY',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'JLR',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'KE1',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'KE2',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'KE3',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'KE6',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'KEB',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'KED',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'KEW',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'LBC',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'LEE',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'LMX',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'LPR',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'LR3',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'LRR',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'MCD',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'MCE',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'MNO',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'MNT',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'MRD',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'MRN',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'MRT',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'NCL',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'PRZ',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'RCR',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'RGN',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'SCR',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'SCS',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'SM3',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'SMD',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'SMN',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'STE',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'STN',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'STT',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'SWT',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'TBT',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'THN',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
//   {
//     code: 'UCU',
//     image: require('../images/buildings/outer_placeholder_2.jpg'),
//   },
//   {
//     code: 'VNR',
//     image: require('../images/buildings/outer_placeholder.jpg'),
//   },
// ];
