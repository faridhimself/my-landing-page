export default function ContactPage() {
  return (
    <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
      <h1 className="mb-8 text-3xl font-bold">Contact Us</h1>
      <div className="grid gap-8 lg:grid-cols-2">
        <div>
          <h2 className="text-xl font-semibold">Get in Touch</h2>
          <div className="mt-4 space-y-4">
            <p className="flex items-center gap-2">
              <span className="font-medium">LinkedIn:</span>
              <a
                href="https://www.linkedin.com/in/faridhimself/"
                className="text-primary hover:underline"
              >
                linkedin.com/in/faridhimself
              </a>
            </p>
            <p className="flex items-center gap-2">
              <span className="font-medium">GitHub:</span>
              <a href="https://github.com/faridhimself/" className="text-primary hover:underline">
                github.com/faridhimself
              </a>
            </p>
            <p className="flex items-center gap-2">
              <span className="font-medium">Email:</span>
              <a href="mailto:faridhimself@gmail.com" className="text-primary hover:underline">
                faridhimself@gmail.com
              </a>
            </p>
            <p className="flex items-center gap-2">
              <span className="font-medium">Phone:</span>
              <a href="tel:+36707434351" className="text-primary hover:underline">
                +36707434351
              </a>
            </p>
            <div className="mt-6">
              <a
                href="https://drive.google.com/uc?export=download&id=1cedcley4KoGYnMv9_QwTpNFXdmRb8Oby"
                className="inline-flex h-9 items-center justify-center rounded-md bg-primary px-4 text-sm font-medium text-primary-foreground shadow transition-colors hover:bg-primary/90"
              >
                Download CV
              </a>
            </div>
          </div>
        </div>
        <div>
          <div
            id="mc_embed_shell"
            dangerouslySetInnerHTML={{
              __html: `
                <link href="//cdn-images.mailchimp.com/embedcode/classic-061523.css" rel="stylesheet" type="text/css">
                <style type="text/css">
                  #mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; width: 600px;}
                </style>
                <div id="mc_embed_signup">
                  <form action="https://productanalytics.us10.list-manage.com/subscribe/post?u=3e9a49a497d2d27b1d488944b&amp;id=06ac7520da&amp;f_id=001446e1f0" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank">
                    <div id="mc_embed_signup_scroll">
                      <h2>Subscribe</h2>
                      <div class="indicates-required"><span class="asterisk">*</span> indicates required</div>
                      <div class="mc-field-group">
                        <label for="mce-EMAIL">Email Address <span class="asterisk">*</span></label>
                        <input type="email" name="EMAIL" class="required email" id="mce-EMAIL" required="" value="">
                      </div>
                      <div id="mce-responses" class="clear foot">
                        <div class="response" id="mce-error-response" style="display: none;"></div>
                        <div class="response" id="mce-success-response" style="display: none;"></div>
                      </div>
                      <div aria-hidden="true" style="position: absolute; left: -5000px;">
                        <input type="text" name="b_3e9a49a497d2d27b1d488944b_06ac7520da" tabindex="-1" value="">
                      </div>
                      <div class="optionalParent">
                        <div class="clear foot">
                          <input type="submit" name="subscribe" id="mc-embedded-subscribe" class="button" value="Subscribe">
                          <p style="margin: 0px auto;">
                            <a href="http://eepurl.com/i6TicU" title="Mailchimp - email marketing made easy and fun">
                              <span style="display: inline-block; background-color: transparent; border-radius: 4px;">
                                <img class="refferal_badge" src="https://digitalasset.intuit.com/render/content/dam/intuit/mc-fe/en_us/images/intuit-mc-rewards-text-dark.svg" alt="Intuit Mailchimp" style="width: 220px; height: 40px; display: flex; padding: 2px 0px; justify-content: center; align-items: center;">
                              </span>
                            </a>
                          </p>
                        </div>
                      </div>
                    </div>
                  </form>
                </div>
                <script type="text/javascript" src="//s3.amazonaws.com/downloads.mailchimp.com/js/mc-validate.js"></script>
                <script type="text/javascript">
                  (function($) {
                    window.fnames = new Array();
                    window.ftypes = new Array();
                    fnames[0]='EMAIL';
                    ftypes[0]='email';
                    fnames[1]='FNAME';
                    ftypes[1]='text';
                    fnames[2]='LNAME';
                    ftypes[2]='text';
                    fnames[3]='ADDRESS';
                    ftypes[3]='address';
                    fnames[4]='PHONE';
                    ftypes[4]='phone';
                    fnames[5]='BIRTHDAY';
                    ftypes[5]='birthday';
                    fnames[6]='COMPANY';
                    ftypes[6]='text';
                  }(jQuery));
                  var $mcj = jQuery.noConflict(true);
                </script>
              `,
            }}
          />
        </div>
      </div>
    </div>
  )
}

