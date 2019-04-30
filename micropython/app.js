var app = new Vue({
    el: '#app',
    data: {
        led: false
    },
    methods: {
        led_change() {
            console.log(this.led);
            $.ajax({url: "/set?led="+(this.led?"on":"off")}).done(data => {
                if(data=='on') { this.led = true; }
                else if(data=='off') { this.led = false; }
                else { console.warn("What is this? "+data); }
            });
        }
    }
});
