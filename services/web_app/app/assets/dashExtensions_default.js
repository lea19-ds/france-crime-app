window.dashExtensions = Object.assign({}, window.dashExtensions, {
    default: {
        function0: function(feature, context) {
            const {
                classes,
                colorscale,
                style,
                colorprop,
                data
            } = context.hideout;
            const departement = feature.properties['code'];

            const value = data[departement]['taux_par_pop'] * 100;

            for (let i = 0; i < classes.length; i++) {
                if (value > classes[i]) {
                    style.fillColor = colorscale[i];
                }
            }
            return style;
        }
    }
});