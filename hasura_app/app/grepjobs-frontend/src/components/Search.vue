<template lang="html">
  <header class="masthead">
    <div class="container h-100">
      <div class="row h-100">
        <div class="col-lg-12 my-auto">
          <div class="mx-auto">
            <div id="gif-container" v-if="!isSearchShown">
              <center>
                <div class="row">
                  <div class="col-md-12">
                    <h1 id="search-title"><strong>Looking for...</strong></h1>
                  </div>
                  <div class="col-md-5">
                    <img id="gif-title" class="gif" v-bind:src="titleGif"/>
                    <h2>{{ this.jobTitle }}</h2>
                  </div>
                  <div class="col-md-2">
                    <img class="gif-sm" v-bind:src="hypeGif"/>
                    <h2 id="search-load">Jobs In</h2>
                  </div>
                  <div class="col-md-5">
                    <img id="gif-location" class="gif" v-bind:src="locationGif"/>
                    <h2>{{ this.jobLocation }}</h2>
                  </div>
                </div>
              </center>
            </div>

            <div id="searchField" v-show="isSearchShown">
              <h1 class="mb-5 search animated fadeInDown">
                  I am looking for a
                  <input id="job-title" class="search-input" :style="{width: this.jobTitle.length * this.paddingTolerance + 'px'}" type="text" v-model='jobTitle' spellcheck="false"/>
                  job
              </h1>
              <h1 class="animated fadeInDown">
                  in <input id="job-location" class="search-input" type="text" :style="{width: this.jobLocation.length * this.paddingTolerance + 'px'}" v-model='jobLocation' spellcheck="false"/>
              </h1>

              <br />

              <div class="text-center animated fadeInDown" v-if="showButton">
                  <div class="btn btn-outline btn-xl animated pulse infinite" v-on:click="findJob">Find your dream job</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Search',
  data () {
    return {
      jobTitle: '',
      titleGif: './static/assets/img/loading.gif',
      jobLocation: '',
      locationGif: './static/assets/img/loading.gif',
      paddingTolerance: 30,
      isSearchShown: true,
      hypeGif: './static/assets/img/loading.gif'
    }
  },
  methods: {
    findJob: function () {
      this.isSearchShown = false
      this.$http.get(`http://api.giphy.com/v1/gifs/search?api_key=c6caa15f718f4a64859883c625d3d5ea&q=${this.jobTitle}&limit=1`).then(response => {
        this.titleGif = response['body']['data']['0']['images']['original']['url']
      },
      response => {
        console.log('Error loading title gif')
      })

      this.$http.get(`http://api.giphy.com/v1/gifs/search?api_key=c6caa15f718f4a64859883c625d3d5ea&q=${this.jobLocation + ' city'}&limit=1`).then(response => {
        this.locationGif = response['body']['data']['0']['images']['original']['url']
      },
      response => {
        console.log('Error loading hype gif')
      })

      // offset allows a unique gif to be shown on each search
      let offset = Math.floor(Math.random() * (100 - 0))
      console.log(offset)
      this.$http.get(`http://api.giphy.com/v1/gifs/search?api_key=c6caa15f718f4a64859883c625d3d5ea&q=excited&limit=1&offset=${offset}`).then(response => {
        this.hypeGif = response['body']['data']['0']['images']['original']['url']
      },
      response => {
        console.log('Error loading location gif')
      })
    }
  },
  computed: {
    showButton: function () {
      if (this.jobTitle.length >= 2 && this.jobLocation.length >= 2) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style lang="css">
</style>
