<template>
  <div>
    <h2>Preposition Check Case by Case</h2>
    <b-container fluid>
      <b-row class="justify-content-center" style="margin-bottom: 8px;">
        <b-col sm="12" md="8" lg="6">
          <b-form-input v-model="arg" :type="'text'" placeholder="Word"></b-form-input>
        </b-col>
      </b-row>
      <b-row class="justify-content-center" style="margin-bottom: 16px;">
        <b-col sm="12" md="8" lg="6">
          <b-form-input v-model="subarg" :type="'text'" placeholder="Preposition"></b-form-input>
        </b-col>
      </b-row>
      <b-row class="justify-content-center">
        <b-button variant="outline-primary" v-on:click="getContent">Search</b-button>
      </b-row>

      <hr />

      <b-row v-for="(item, index) in res" :key="index" class="justify-content-center">
        <b-col sm="12" md="8" lg="6">
          <b-card no-body class="mb-1">
            <b-card-body>
              <b-card-text>{{ item }}</b-card-text>
            </b-card-body>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'PrepositionCheckCaseByCase',
  data() {
    return {
      arg: '',
      subarg: '',
      res: []
    };
  },
  methods: {
    getContent: function(event) {
      this.$http
        .get('/api/preposition_check_case_by_case', {
          params: { arg: this.arg, subarg: this.subarg }
        })
        .then(response => {
          this.res = response.data;
          console.log(response);
        })
        .catch(response => console.log(response));
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
</style>
