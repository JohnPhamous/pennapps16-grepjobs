Vue.component('job-listing', {
  template: `
    <div>
      <div class="listing" v-for="job in jobs">
        <div class="listing-info">
          <h2 style="font-weight:600">{{ job.title }}</h2>
          <p>{{ job.company }}</p>
          <p>{{ job.location }}</p>
          <p>{{ job.wage }}</p>
        </div>
        <div class="row text-center actions-container">
          <div class="col-md-6 listing-actions">
            <p>18C</p>
          </div>
          <div class="col-md-6 listing-actions">
            <strong>
              <p v-if="job.isGrowing === 1" style="color: #4cffa7">Growing</p>
              <p v-if="job.isGrowing === 0" style="color: #ffb641">Stagnant</p>
              <p v-if="job.isGrowing === -1" style="color: #FF2629">Shrinking</p>
            </strong>
          </div>
          <div class="apply-btn col-md-12">
            <a class="btn btn-primary btn-sm" v-bind:href="job.url">Apply</a>
          </div>
        </div>
      </div>
    </div>
  `,
  data: function() {
    return {
      jobs: [
        {
          title: 'Web Developer',
          company: 'NASA JPL',
          wage: '$80,000',
          location: 'Pasadena, CA',
          url: '#',
          isGrowing: 1
        },
        {
          title: 'Software Engineer',
          company: 'Awesome Startup',
          wage: '$90,000',
          location: 'Pleasanton, CA',
          url: '#',
          isGrowing: -1
        }
      ]
    }
  }
})

var app = new Vue({
  el: '#hud'
})
