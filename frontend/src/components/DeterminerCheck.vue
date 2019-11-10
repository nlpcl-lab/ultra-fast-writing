<template>
  <div>
    <h2 style="margin-bottom: 12px;">Determiner Check</h2>
    <b-container fluid>
      <b-row class="justify-content-center" style="margin-bottom: 16px;">
        <b-col sm="12" md="8" lg="6">
          <b-form-input v-model="arg" :type="'text'" placeholder="Word"></b-form-input>
        </b-col>
      </b-row>
      <b-row class="justify-content-center">
        <b-button variant="outline-primary" v-on:click="getContent">Search</b-button>
      </b-row>

      <hr />

      <b-card no-body class="mb-1" v-if="Object.keys(res_count).length !== 0">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block href="#" v-b-toggle.accordion-2 variant="info">{{ res_count }}</b-button>
        </b-card-header>
        <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-card-text>{{ res_sents }}</b-card-text>
          </b-card-body>
        </b-collapse>
      </b-card>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'DeterminerCheck',
  data() {
    return {
      arg: '',
      res_count: {},
      res_sents: {}
    };
  },
  methods: {
    getContent: function(event) {
      this.$http
        .get('/api/determiner_check', { params: { arg: this.arg } })
        .then(response => {
          this.res_count = response.data.count;
          this.res_sents = response.data.sentence;
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
