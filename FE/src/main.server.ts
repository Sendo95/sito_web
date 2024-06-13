import { bootstrapApplication } from '@angular/platform-browser';
import { config } from './app/app.config.server';
import { TemplateSitoComponent } from './app/template-sito/template-sito.component';

const bootstrap = () => bootstrapApplication(TemplateSitoComponent, config);

export default bootstrap;