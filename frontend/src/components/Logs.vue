<template>
  <div>
    <h2>Logs</h2>
    <b-container fluid>
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
  name: 'Logs',
  data() {
    return {
      res: []
    };
  },
  mounted() {
    this.$http
      .get('/api/log')
      .then(response => {
        this.res = response.data.reverse();
        console.log(response);
      })
      .catch(response => console.log(response));
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
a {
  color: #42b983;
}
</style>
