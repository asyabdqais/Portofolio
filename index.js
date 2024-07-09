particlesJS("backgrond", {
    

    particles: {
        number: {
            value: 15, // Number Of Particles (Count)
            density: {
                enable: true,
                value_area:300 // Area Where particles will distributed

            },
        },

        color: {
            value: "#ffffff", // particles color
        },
        shape: {
            type: "triangle", // Shape type
        },
        opacity: {
            value: 0.8, // Base opacity of particles 
            random: true, 
            anum: {
                enable: true,
                speed: 1,
                opacity_min: 0.1,
                sync: false, 
            },
       },
       size: {
        value: 5, // Base size of particles
        random: true,
        anim: {
            enable: true,
            speed: 4,
            size_min: 0.3,
            synce: false,
        },
       },

       // Connecting lines
       line_linked: {
            enable: true,
            distance: 150, // Maximum distance between linked particles
            color: "#ffffff",
            opacity: 0.4,
            width: 1,
       },
   
    },


})