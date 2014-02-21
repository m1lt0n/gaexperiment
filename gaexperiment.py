EXPERIMENT_CODE = """<!-- Google Analytics Content Experiment code -->
<script>function utmx_section(){}function utmx(){}(function(){var
k='%(experiment_code)s',d=document,l=d.location,c=d.cookie;
if(l.search.indexOf('utm_expid='+k)>0)return;
function f(n){if(c){var i=c.indexOf(n+'=');if(i>-1){var j=c.
indexOf(';',i);return escape(c.substring(i+n.length+1,j<0?c.
length:j))}}}var x=f('__utmx'),xx=f('__utmxx'),h=l.hash;d.write(
'<sc'+'ript src="'+'http'+(l.protocol=='https:'?'s://ssl':
'://www')+'.google-analytics.com/ga_exp.js?'+'utmxkey='+k+
'&utmx='+(x?x:'')+'&utmxx='+(xx?xx:'')+'&utmxtime='+new Date().
valueOf()+(h?'&utmxhash='+escape(h.substr(1)):'')+
'" type="text/javascript" charset="utf-8"><\/sc'+'ript>')})();
</script><script>utmx('url','A/B');</script>
<!-- End of Google Analytics Content Experiment code -->
"""


class GaExperiment(object):
    VARIATION_PARAM = 'gaexp'

    """
    The GaExperiment object handles the creation of the google experiment
    code to be inserted in a template in order to enable the google experiment
    functionality.
    """
    def __init__(self, experiment_code, whitelist, get_vars):
        self.experiment_code = experiment_code
        self.whitelist = whitelist
        self.get_vars = get_vars

    def template_to_serve(self, original_template):
        """
        Returns the template to be served, based on the whitelist provided.
        If an invalid version is provided, the original page is served. This
        code is here to avoid having a change in the version GET variable and
        throwing an error on the browser.
        """
        if self.is_original_version:
            return original_template

        exp_param = self.get_vars[self.VARIATION_PARAM]
        if exp_param in self.whitelist:
            base, ext = original_template.split('.', 1)
            return '%s_%s.%s' % (base, exp_param, ext)

        return original_template

    @property
    def is_original_version(self):
        return self.VARIATION_PARAM not in self.get_vars

    @property
    def code(self):
        if not self.is_original_version:
            return '<!-- Google Experiments Variation Page -->'

        return EXPERIMENT_CODE % {'experiment_code': self.experiment_code}
