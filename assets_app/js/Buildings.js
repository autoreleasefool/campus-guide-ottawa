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

module.exports = [

  {
    code: 'MHN',
    image: require('../images/buildings/outer_placeholder.jpg'),
    name_en: 'Hamelin Hall',
    name_fr: 'Pavillon Hamelin',
    lat: 45.4238072,
    long: -75.6879882,
    address_en: '70 Laurier Avenue East',
    address_fr: '70, avenue Laurier est',
    facilities: [
      'food',
      'printer',
      'library',
      'parking',
    ],
    default_room_type: 5,
    rooms: [
      {
        name: '02',
        type: 6,
        alt_name_en: 'Julien Couture Resource Centre',
        alt_name_fr: 'Centre de ressources Julien-Couture',
      },
      {
        name: '03',
      },
      {
        name: '04',
      },
      {
        name: '05',
      },
      {
        name: '06',
      },
      {
        name: '07',
      },
      {
        name: '08',
      },
      {
        name: '09',
      },
      {
        name: '010',
      },
      {
        name: '012',
      },
      {
        name: '013',
      },
      {
        name: '015',
      },
      {
        name: '016',
      },
      {
        name: '017',
      },
      {
        name: '018',
      },
      {
        name: '019',
      },
      {
        name: '020',
        type: 15,
        alt_name_en: 'J.A. Bombardier Foundation Room',
        alt_name_fr: 'Salle Fondation J.A. Bombardier',
      },
      {
        name: '021',
      },
      {
        name: '022',
      },
      {
        name: '023',
      },
      {
        name: '024',
      },
      {
        name: '025',
      },
      {
        name: '026',
      },
      {
        name: '027',
      },
      {
        name: '028',
      },
      {
        name: '029',
      },
      {
        name: '030',
        type: 2,
        alt_name: 'GO Café',
      },
      {
        name: '033',
        type: 1,
      },
      {
        name: '100',
      },
      {
        name: '101',
      },
      {
        name: '102',
      },
      {
        name: '103',
      },
      {
        name: '104',
      },
      {
        name: '105',
      },
      {
        name: '106',
      },
      {
        name: '107',
      },
      {
        name: '108',
      },
      {
        name: '109',
      },
      {
        name: '110',
      },
      {
        name: '111',
        type: 11,
        alt_name_en: 'Graduate Student Association',
        alt_name_fr: 'Association des étudiants diplômés',
      },
      {
        name: '112',
      },
      {
        name: '113',
        type: 13,
      },
      {
        name: '114',
      },
      {
        name: '115',
      },
      {
        name: '116',
        type: 20,
      },
      {
        name: '117',
        type: 11,
        alt_name_en: 'Language Testing Services',
        alt_name_fr: 'Services d\'evaluation linguistique',
      },
      {
        name: '118',
      },
      {
        name: '119',
        type: 20,
      },
      {
        name: '120',
      },
      {
        name: '121',
      },
      {
        name: '122',
      },
      {
        name: '123',
      },
      {
        name: '124',
      },
      {
        name: '125',
      },
      {
        name: '126',
      },
      {
        name: '127',
      },
      {
        name: '130',
        type: 11,
        alt_name_en: 'OLBI',
        alt_name_fr: 'ILOB',
      },
      {
        name: '131',
      },
      {
        name: '133',
      },
      {
        name: '134',
      },
      {
        name: '135',
      },
      {
        name: '136',
      },
      {
        name: '137',
      },
      {
        name: '138',
      },
      {
        name: '139',
      },
      {
        name: '140',
        type: 13,
      },
      {
        name: '141',
      },
      {
        name: '142',
        type: 14,
      },
      {
        name: '143',
      },
      {
        name: '144',
      },
      {
        name: '145',
        type: 12,
      },
      {
        name: '201',
      },
      {
        name: '202',
      },
      {
        name: '203',
      },
      {
        name: '204',
      },
      {
        name: '205',
      },
      {
        name: '206',
      },
      {
        name: '207',
      },
      {
        name: '208',
      },
      {
        name: '210',
      },
      {
        name: '211',
      },
      {
        name: '212',
      },
      {
        name: '213',
      },
      {
        name: '215',
        type: 16,
        alt_name_en: 'Scotiabank Room',
        alt_name_fr: 'Salle Banque Scotia',
      },
      {
        name: '216',
      },
      {
        name: '217',
      },
      {
        name: '218',
      },
      {
        name: '219',
      },
      {
        name: '220',
      },
      {
        name: '221',
      },
      {
        name: '222',
      },
      {
        name: '223',
      },
      {
        name: '224',
      },
      {
        name: '225',
      },
      {
        name: '227',
      },
      {
        name: '228',
      },
      {
        name: '229',
      },
      {
        name: '231',
      },
      {
        name: '232',
      },
      {
        name: '233',
        type: 14,
      },
      {
        name: '234',
        type: 11,
        alt_name_en: 'Modern Languages and Literature Secretariat',
        alt_name_fr: 'Sécretariat des langues et littératures modernes',
      },
      {
        name: '235',
      },
      {
        name: '236',
      },
      {
        name: '237',
      },
      {
        name: '238',
      },
      {
        name: '239',
      },
      {
        name: '240',
      },
      {
        name: '241',
      },
      {
        name: '242',
      },
      {
        name: '243',
      },
      {
        name: '244',
      },
      {
        name: '245',
      },
      {
        name: '246',
        type: 12,
      },
      {
        name: '247',
      },
      {
        name: '248',
      },
      {
        name: '249',
      },
      {
        name: '250',
      },
      {
        name: '251',
      },
      {
        name: '252',
      },
      {
        name: '253',
      },
      {
        name: '257',
        type: 1,
      },
      {
        name: '301',
        type: 12,
      },
      {
        name: '302',
      },
      {
        name: '303',
      },
      {
        name: '304',
      },
      {
        name: '305',
      },
      {
        name: '306',
      },
      {
        name: '307',
      },
      {
        name: '308',
      },
      {
        name: '309',
      },
      {
        name: '310',
      },
      {
        name: '311',
      },
      {
        name: '313',
      },
      {
        name: '314',
      },
      {
        name: '315',
      },
      {
        name: '316',
      },
      {
        name: '318',
        type: 16,
        alt_name_en: 'Metropolitan Life Room',
        alt_name_fr: 'Salle La Métropolitaine',
      },
      {
        name: '319',
      },
      {
        name: '320',
      },
      {
        name: '321',
        type: 11,
        alt_name: 'Undergraduate English Students\' Association',
      },
      {
        name: '322',
      },
      {
        name: '323',
      },
      {
        name: '324',
      },
      {
        name: '325',
      },
      {
        name: '326',
      },
      {
        name: '327',
      },
      {
        name: '328',
      },
      {
        name: '329',
      },
      {
        name: '330',
      },
      {
        name: '332',
      },
      {
        name: '334',
      },
      {
        name: '335',
      },
      {
        name: '336',
      },
      {
        name: '337',
      },
      {
        name: '338',
        type: 11,
        alt_name_en: 'English Secretariat',
        alt_name_fr: 'Sécretariat des anglais',
      },
      {
        name: '339',
      },
      {
        name: '340',
      },
      {
        name: '341',
      },
      {
        name: '342',
      },
      {
        name: '343',
      },
      {
        name: '344',
      },
      {
        name: '345',
      },
      {
        name: '346',
      },
      {
        name: '347',
      },
      {
        name: '348',
      },
      {
        name: '349',
      },
      {
        name: '350',
        type: 16,
      },
      {
        name: '351',
      },
      {
        name: '352',
      },
      {
        name: '353',
      },
      {
        name: '354',
      },
      {
        name: '355',
      },
      {
        name: '356',
      },
      {
        name: '401',
        type: 11,
        alt_name_en: 'Linguistics, Translation and Interpretation Secretariat',
        alt_name_fr: 'Sécretariat des linguistique, traduction et interprétation',
      },
      {
        name: '402',
      },
      {
        name: '403',
      },
      {
        name: '404',
      },
      {
        name: '405',
      },
      {
        name: '406',
      },
      {
        name: '407',
      },
      {
        name: '408',
      },
      {
        name: '409',
      },
      {
        name: '410',
      },
      {
        name: '411',
      },
      {
        name: '412',
      },
      {
        name: '413',
      },
      {
        name: '415',
      },
      {
        name: '416',
      },
      {
        name: '417',
      },
      {
        name: '418',
      },
      {
        name: '420',
        type: 16,
        alt_name_en: 'CIBC Room',
        alt_name_fr: 'Salle CIBC',
      },
      {
        name: '421',
      },
      {
        name: '422',
      },
      {
        name: '423',
      },
      {
        name: '424',
      },
      {
        name: '425',
      },
      {
        name: '426',
      },
      {
        name: '428',
      },
      {
        name: '429',
      },
      {
        name: '430',
      },
      {
        name: '432',
      },
      {
        name: '433',
      },
      {
        name: '434',
      },
      {
        name: '435',
      },
      {
        name: '436',
        type: 12,
        alt_name_en: 'Salon Monet Room',
        alt_name_fr: 'Salle Salon Monet',
      },
      {
        name: '437',
      },
      {
        name: '438',
      },
      {
        name: '439',
      },
      {
        name: '440',
      },
      {
        name: '441',
      },
      {
        name: '442',
      },
      {
        name: '443',
      },
      {
        name: '444',
      },
      {
        name: '445',
      },
      {
        name: '446',
      },
      {
        name: '447',
      },
      {
        name: '448',
      },
      {
        name: '449',
      },
      {
        name: '450',
      },
      {
        name: '451',
      },
      {
        name: '452',
      },
      {
        name: '501',
        type: 11,
        alt_name_en: 'Digital Humanities',
        alt_name_fr: 'Sciences humaines numériques',
      },
      {
        name: '502',
      },
      {
        name: '503',
      },
      {
        name: '504',
      },
      {
        name: '505',
      },
      {
        name: '506',
        type: 12,
        alt_name_en: 'Brian Harris Room',
        alt_name_fr: 'Salle Brian Harris',
      },
      {
        name: '507',
      },
      {
        name: '509',
        type: 12,
      },
      {
        name: '511',
      },
      {
        name: '513',
        type: 19,
      },
      {
        name: '515',
      },
      {
        name: '516',
      },
      {
        name: '517',
      },
      {
        name: '518',
      },
      {
        name: '519',
      },
      {
        name: '520',
      },
      {
        name: '521',
      },
      {
        name: '522',
      },
      {
        name: '523',
        type: 16,
      },
      {
        name: '524',
      },
      {
        name: '525',
      },
      {
        name: '526',
        type: 11,
        alt_name_en: 'Faculty of Arts Writing Centre',
        alt_name_fr: 'Centre d\'écriture de la faculté des arts',
      },
      {
        name: '527',
      },
      {
        name: '528',
      },
      {
        name: '529',
      },
      {
        name: '530',
      },
      {
        name: '531',
      },
    ],
  },
];
