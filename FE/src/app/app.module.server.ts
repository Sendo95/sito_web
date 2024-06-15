import { NgModule } from '@angular/core';
import { ServerModule } from '@angular/platform-server';

import { AppModule } from './app.module';
import { TemplateSitoComponent } from './template-sito/template-sito.component';

@NgModule({
  imports: [
    AppModule,
    ServerModule,
  ],
  bootstrap: [TemplateSitoComponent],
})
export class AppServerModule {}
