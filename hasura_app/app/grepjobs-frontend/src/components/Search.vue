<template lang="html">
  <header class="masthead">
    <div class="container h-100">
      <div class="row h-100">
        <div class="col-lg-12 my-auto">
          <div class="mx-auto">
              <div id="gif-container" v-if="!isSearchShown">
                <center>
                  <h1 id="search-title">Searching...</h1>
                  <img id="gif-title" class="gif" src="https://media2.giphy.com/media/3ohze15TQsHnWxQfm0/giphy.gif"/>
                  <img id="gif-location" class="gif" src="https://media0.giphy.com/media/pTeT1LFAWfQEo/giphy.gif"/>
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
                <div class="text-center animated fadeInDown">
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
      jobLocation: '',
      paddingTolerance: 30,
      isSearchShown: true
    }
  },
  methods: {
    findJob: function () {
      this.isSearchShown = false
    }
  }
}
</script>

<style lang="css">
</style>
