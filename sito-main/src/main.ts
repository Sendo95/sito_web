import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { TemplateSitoComponent } from './app/template-sito/template-sito.component';

bootstrapApplication(TemplateSitoComponent, appConfig)
  .catch((err) => console.error(err));
