import React from 'react';
import { Mail, Phone } from 'lucide-react';

const Contact = () => {
  return (
    <div className="min-h-screen bg-gray-50 py-12">
      <div className="max-w-7xl mx-auto px-4">
        <div className="bg-white rounded-lg shadow-md p-8">
          <h1 className="text-4xl font-bold mb-8">Contact Us</h1>
          
          <div className="grid md:grid-cols-2 gap-8">
            <div>
              <div className="mb-8">
                <div className="flex items-center mb-4">
                  <Mail className="h-5 w-5 mr-2 text-blue-600" />
                  <a href="mailto:faridhimself@gmail.com" className="text-blue-600 hover:underline">
                    faridhimself@gmail.com
                  </a>
                </div>
                <div className="flex items-center">
                  <Phone className="h-5 w-5 mr-2 text-blue-600" />
                  <a href="tel:+36707434351" className="text-blue-600 hover:underline">
                    +36707434351
                  </a>
                </div>
              </div>

              <div className="mb-8">
                <h3 className="text-xl font-semibold mb-4">Newsletter Signup</h3>
                <div id="mc_embed_shell">
                  <link href="//cdn-images.mailchimp.com/embedcode/classic-061523.css" rel="stylesheet" type="text/css" />
                  <div id="mc_embed_signup">
                    <form action="https://productanalytics.us10.list-manage.com/subscribe/post?u=3e9a49a497d2d27b1d488944b&amp;id=06ac7520da&amp;f_id=001546e1f0" 
                          method="post" 
                          id="mc-embedded-subscribe-form" 
                          name="mc-embedded-subscribe-form" 
                          className="validate" 
                          target="_blank">
                      <div id="mc_embed_signup_scroll">
                        <div className="indicates-required"><span className="asterisk">*</span> indicates required</div>
                        <div className="mc-field-group">
                          <label htmlFor="mce-EMAIL">Email Address <span className="asterisk">*</span></label>
                          <input type="email" name="EMAIL" className="required email" id="mce-EMAIL" required />
                        </div>
                        <div id="mce-responses" className="clear foot">
                          <div className="response" id="mce-error-response" style={{display: 'none'}}></div>
                          <div className="response" id="mce-success-response" style={{display: 'none'}}></div>
                        </div>
                        <div aria-hidden="true" style={{position: 'absolute', left: '-5000px'}}>
                          <input type="text" name="b_3e9a49a497d2d27b1d488944b_06ac7520da" tabIndex={-1} />
                        </div>
                        <div className="optionalParent">
                          <div className="clear foot">
                            <input type="submit" name="subscribe" id="mc-embedded-subscribe" className="button" value="Subscribe" />
                          </div>
                        </div>
                      </div>
                    </form>
                  </div>
                  <script type="text/javascript" src="//s3.amazonaws.com/downloads.mailchimp.com/js/mc-validate.js"></script>
                </div>
              </div>
            </div>

            <div>
              <form className="space-y-6">
                <div>
                  <label htmlFor="name" className="block text-sm font-medium text-gray-700">Name</label>
                  <input
                    type="text"
                    id="name"
                    className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                  />
                </div>
                <div>
                  <label htmlFor="email" className="block text-sm font-medium text-gray-700">Email</label>
                  <input
                    type="email"
                    id="email"
                    className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                  />
                </div>
                <div>
                  <label htmlFor="message" className="block text-sm font-medium text-gray-700">Message</label>
                  <textarea
                    id="message"
                    rows={4}
                    className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                  ></textarea>
                </div>
                <button
                  type="submit"
                  className="w-full bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700"
                >
                  Send Message
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact;