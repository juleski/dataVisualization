import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { DatePipe } from '@angular/common';

import { AppComponent } from './app.component';

import { ChartsModule } from 'ng2-charts';
import { ESDataService } from './esdata.service';
import { FrquencyChartComponent } from './frquency-chart/frquency-chart.component';


@NgModule({
  declarations: [
    AppComponent,
    FrquencyChartComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    ChartsModule
  ],
  providers: [
    DatePipe,
    ESDataService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
