<template>
  <div id="app">
    <router-link :to="'/'">
      <img src="./assets/logo.png" style="max-width: 160px;" />
      <h1 id="header" style="margin-bottom: 12px">UltraFastBONO</h1>
      <br />
    </router-link>
    <div style="margin-bottom: 24px;">
      <b-button-group style="margin-bottom: 4px;">
        <b-button to="/determiner_check">Determiner Check</b-button>
        <b-button to="/determiner_check_case_by_case">Determiner Check Case by Case</b-button>
      </b-button-group>
      <b-button-group style="margin-bottom: 4px;">
        <b-button to="/check_word_usage">Check Word Usage</b-button>
        <b-button to="/check_phrase_usage">Check Phrase Usage</b-button>
      </b-button-group>
      <b-button-group style="margin-bottom: 4px;">
        <b-button to="/preposition_check">Preposition Check</b-button>
        <b-button to="/preposition_check_case_by_case">Preposition Check Case by Case</b-button>
      </b-button-group>
      <b-button-group style="margin-bottom: 4px;">
        <b-button to="/logs">Logs</b-button>
      </b-button-group>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Permanent+Marker&display=swap');

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#header {
  font-family: 'Permanent Marker', cursive !important;
  color: #2196f3;
}
</style>
