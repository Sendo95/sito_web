import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';
import { TemplateSitoComponent } from './app/template-sito/template-sito.component';


platformBrowserDynamic().bootstrapModule(TemplateSitoComponent)
  .catch(err => console.error(err));
