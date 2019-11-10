import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '@/components/HelloWorld';
import DeterminerCheck from '@/components/DeterminerCheck';
import DeterminerCheckCaseByCase from '@/components/DeterminerCheckCaseByCase';
import CheckWordUsage from '@/components/CheckWordUsage';
import CheckPhraseUsage from '@/components/CheckPhraseUsage';
import PrepositionCheck from '@/components/PrepositionCheck';
import PrepositionCheckCaseByCase from '@/components/PrepositionCheckCaseByCase';
import Logs from '@/components/Logs';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/determiner_check',
      name: 'DeterminerCheck',
      component: DeterminerCheck
    },
    {
      path: '/determiner_check_case_by_case',
      name: 'DeterminerCheckCaseByCase',
      component: DeterminerCheckCaseByCase
    },
    {
      path: '/check_word_usage',
      name: 'CheckWordUsage',
      component: CheckWordUsage
    },
    {
      path: '/check_phrase_usage',
      name: 'CheckPhraseUsage',
      component: CheckPhraseUsage
    },
    {
      path: '/preposition_check',
      name: 'PrepositionCheck',
      component: PrepositionCheck
    },
    {
      path: '/preposition_check_case_by_case',
      name: 'PrepositionCheckCaseByCase',
      component: PrepositionCheckCaseByCase
    },
    {
      path: '/logs',
      name: 'Logs',
      component: Logs
    }
  ]
});
