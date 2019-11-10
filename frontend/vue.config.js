module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:5678/api',
        ws: true,
        changeOrigin: true
      }
    }
  }
};
