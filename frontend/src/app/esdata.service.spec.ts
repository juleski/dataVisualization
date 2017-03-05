/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { ESDataService } from './esdata.service';

describe('ESDataService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ESDataService]
    });
  });

  it('should ...', inject([ESDataService], (service: ESDataService) => {
    expect(service).toBeTruthy();
  }));
});
